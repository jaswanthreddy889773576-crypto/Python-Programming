# Week 4 - Task 3: Python Libraries
# Objective: Demonstrate random, math, and datetime libraries.
# Import required Python libraries
import random
import math
import datetime
# Example 1: Random Library
# Generates a random integer between 1 and 100.
print("Example 1: Random Library")
random_number = random.randint(1, 100)
print("Generated Random Number:", random_number)
# Example 2: Math Library
# Calculates the square root and power of a number.
print("\nExample 2: Math Library")
number = 25
square_root = math.sqrt(number)
power_result = math.pow(number, 2)
print("Number:", number)
print("Square Root:", square_root)
print("Power (25 squared):", power_result)
# Example 3: Datetime Library
# Displays the current date and time.
print("\nExample 3: Datetime Library")
current_datetime = datetime.datetime.now()
print("Current Date:", current_datetime.strftime("%d-%m-%Y"))
print("Current Time:", current_datetime.strftime("%H:%M:%S"))
print("\nProgram completed successfully.")
