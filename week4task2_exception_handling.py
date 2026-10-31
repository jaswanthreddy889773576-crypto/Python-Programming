# Week 4 - Task 2: Exception Handling
# Objective: Handle common runtime errors using try-except blocks.
# Example 1: Handling invalid user input
print("Example 1: Invalid Input")
try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Error: Invalid input! Please enter an integer.")
# Example 2: Handling division by zero
print("\nExample 2: Division by Zero")
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
# Example 3: Handling a file not found error
print("\nExample 3: File Not Found")
try:
    file_name = input("Enter the file name to read: ")
    with open(file_name, "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print("Error: The specified file was not found.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
print("\nProgram completed.")
