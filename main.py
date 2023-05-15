# This program is a simple calculator that can add, subtract, multiply, and divide.
# This is run as terminal.
# Define the functions for each operation.
def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y
# Get the user's input for the first number.
print("What is the first number?")
first_number = int(input())
# Get the user's input for the second number.
print("What is the second number?")
second_number = int(input())
# Get the user's input for the operation.
print("What operation would you like to perform? (add, subtract, multiply, divide)")
operation = input()
# Perform the operation and print the result.
if operation == "add":
  print(first_number, "+", second_number, "=", add(first_number, second_number))
elif operation == "subtract":
  print(first_number, "-", second_number, "=", subtract(first_number, second_number))
elif operation == "multiply":
  print(first_number, "*", second_number, "=", multiply(first_number, second_number))
elif operation == "divide":
  print(first_number, "/", second_number, "=", divide(first_number, second_number))
else:
  print("Invalid operation.")