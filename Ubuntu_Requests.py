import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def get_filename_from_url(url, response):
    #Extract filename from URL 
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # If no filename in URL, check Content-Disposition header
    if not filename and 'content-disposition' in response.headers:
        content_disposition = response.headers['content-disposition']
        if 'filename=' in content_disposition:
            filename = content_disposition.split('filename=')[1].strip('"\'')
    
    # If still no filename, generate one with proper extension
    if not filename:
        content_type = response.headers.get('content-type', '').split('/')[-1]
        if content_type in ['jpeg', 'png', 'gif', 'bmp', 'webp']:
            filename = f"downloaded_image.{content_type}"
        else:
            filename = "downloaded_image.jpg"
    
    return filename

def calculate_file_hash(filepath):
    """Calculate MD5 hash of a file to check for duplicates"""
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def is_safe_to_download(response):
    """Check if the response appears to be a safe image file"""
    content_type = response.headers.get('content-type', '').lower()
    
    # Check if content type is an image
    if not content_type.startswith('image/'):
        return False, f"Content type is not an image: {content_type}"
    
    # Check content length to avoid excessively large files
    content_length = response.headers.get('content-length')
    if content_length and int(content_length) > 10 * 1024 * 1024:  # 10MB limit
        return False, f"File too large: {int(content_length) / (1024*1024):.2f}MB"
    
    return True, "Safe to download"

def download_image(url, download_dir):
    """Download a single image with safety checks"""
    try:
        # Set a user-agent header to identify ourselves
        headers = {
            'User-Agent': 'UbuntuImageFetcher/1.0 (Community Tool for Educational Purposes)'
        }
        
        # Make HEAD request first to check headers
        head_response = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
        head_response.raise_for_status()
        
        # Check if safe to download
        is_safe, message = is_safe_to_download(head_response)
        if not is_safe:
            return False, message
        
        # Now make the actual GET request
        response = requests.get(url, headers=headers, timeout=30, stream=True)
        response.raise_for_status()
        
        # Verify content type again in case it changed
        is_safe, message = is_safe_to_download(response)
        if not is_safe:
            return False, message
        
        # Get filename
        filename = get_filename_from_url(url, response)
        filepath = os.path.join(download_dir, filename)
        
        # Check for duplicates by content
        if os.path.exists(filepath):
            # Calculate hash of existing file
            existing_hash = calculate_file_hash(filepath)
            
            # Calculate hash of new content
            new_hash = hashlib.md5(response.content).hexdigest()
            
            if existing_hash == new_hash:
                return True, f"Duplicate image not downloaded: {filename}"
        
        # Save the image
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return True, f"Successfully fetched: {filename}"
        
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {e}"
    except Exception as e:
        return False, f"An error occurred: {e}"

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    print("Ubuntu Principle: I am because we are")
    print("We connect to the global community with respect and gratitude\n")
    
    # Create directory if it doesn't exist
    download_dir = "Fetched_Images"
    os.makedirs(download_dir, exist_ok=True)
    
    # Get URLs from user
    urls_input = input("Please enter image URLs (separated by commas): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]
    
    if not urls:
        print("No URLs provided. Exiting.")
        return
    
    print(f"\nAttempting to fetch {len(urls)} image(s)...\n")
    
    success_count = 0
    for i, url in enumerate(urls, 1):
        print(f"Processing URL {i}/{len(urls)}: {url}")
        
        success, message = download_image(url, download_dir)
        
        if success:
            print(f"✓ {message}")
            success_count += 1
        else:
            print(f"✗ {message}")
        
        print()  # Empty line for readability
    
    print(f"Processed {len(urls)} URLs. Successfully fetched {success_count} image(s).")
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()