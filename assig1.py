num1 = float(input("Enter first number:"))
operator = input("Enter operator (+,-,*,/):")
num2 = float(input("Enter second number:"))

def add (num1,num2):
  return num1 + num2
def subtract (num1,num2):
  return num1 - num2
def multiply (num1,num2):
  return num1 * num2
def divide (num1,num2):
  if num2 != 0:
    return num1 / num2
  else:
    return "Error! Division by zero is undefined."
  
def result (num1, operator, num2):
  if operator == "+":
    return add(num1,num2)
  elif operator == "-":
    return subtract(num1,num2)
  elif operator == "*":
    return multiply(num1,num2)
  elif operator == "/":
    return divide(num1,num2)
  else:
    return "Error! Invalid operator."

output = result(num1, operator, num2)  
print (f"{num1} {operator} {num2} = {output}")