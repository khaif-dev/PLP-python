# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price,discount_percent):
  if discount_percent >= 0.2:
    price = price - (discount_percent*price)
  else:
    price = price
  return (price)
discounted_price = calculate_discount(900,0.1)
print(discounted_price)
discounted_price = calculate_discount(1200,0.4)
print(discounted_price)

# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount():
  Original_price = float(input("Please Enter the original price:"))
  discountPercentage = float(input("Please Enter the percentage discount:"))
  discount_percent = discountPercentage/100
  if discount_percent >= 0.2:
    price = Original_price - (discount_percent*Original_price)
  else:
    price = Original_price
  return (price)

print(f"Your bill is {calculate_discount()}")
