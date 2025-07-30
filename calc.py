#Asking user for the input and storing them as floats
num1 = float(input("Enter firstNumber:"))
operation = (input("Enter operation(+,-,*,/):"))
num2 = float(input("Enter secondNumber:"))

#function to add two numbers
def add(num1, num2):
  return num1 + num2
#function to subtract two numbers
def subtract(num1, num2):
  return num1 - num2
#function to multiply two numbers
def multiply(num1, num2):
  return num1 * num2
#function to divide two numbers
def divide(num1, num2):
  if num2 == 0:
    return "Error!, Division by zero is undefined."
  else:
    return num1 / num2

#function to output the results
def results(num1, operation, num2):
  if operation == "+":
    return add(num1, num2)
  elif operation == "-":
    return subtract(num1, num2)
  elif operation == "*":
   return multiply(num1, num2)
  elif operation == "/":
    return divide(num1, num2)
  else:
    print("Invalid operation")

#call function and display results
output = results(num1, operation, num2)  
print(f"{num1} {operation} {num2} = {output}")  


