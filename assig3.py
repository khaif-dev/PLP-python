# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent)
#  as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(price, discount_percent):
    if discount_percent>= 20:
        final_price = price - (price* (discount_percent/100))
    else:
        final_price = price
    return final_price        
        
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.
try:
    price = float(input("Please Enter Price in Ksh:"))
    percentage_discount = float(input("Please Enter Percentage Discount:"))

    if price <= 0 or percentage_discount <= 0:
        print("Please Enter a valid Price and Percentage Discount")
    else:
        final_price = calculate_discount(price, percentage_discount)
        print(f"The final price after discount is: Ksh {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")           