# writing into the file
file = open('input.txt','w')
file.write("""
Read the contents of input.text.
Count the number of words in the file.
Convert all text to uppercase.
Write the processed text and the word count to a new file called output.txt
Print a success message once the new file is created""")

# reading the file content
file = open('input.txt','r')
data = file.read()
print(data)

# count the no of words in the file
words = data.split()
word_count = len(words)
print(f"Your file has {word_count} number of words")

# converting all text to uppercase
uppercase = data.upper()
print(uppercase)

# writing the processed text and word count in output.txt
with open ('output.txt','w') as output:
  output.write(uppercase + "\n\n")
  output.write(f"word count: {word_count}" )

# ask user for a file name
user_input = input("Please Enter a file name with extension (name.txt,name.pdf,name.csv):")
try:
  user_file = open(user_input,'r')
  content = user_file.read()
  user_file.close()
  print('Found your file')
except FileNotFoundError:
  print('File does not exist')  




