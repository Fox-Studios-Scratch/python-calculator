def add(x, y):
  """Returns the sum of two numbers."""
  return x + y

def subtract(x, y):
  """Returns the difference of two numbers."""
  return x - y

def multiply(x, y):
  """Returns the product of two numbers."""
  return x * y

def divide(x, y):
  """Returns the quotient of two numbers."""
  return x / y

def calculate():
  """Prompts the user for two numbers and an operation, then performs the operation and displays the result."""

  # Get the user's input.
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter an operator (+, -, *, or /): ")

  # Perform the operation.
  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operator.")
    return

  # Display the result.
  print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
  calculate()
