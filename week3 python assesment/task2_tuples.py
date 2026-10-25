# Creating a tuple
numbers = (10, 20, 30, 40, 50)
print("Original tuple:", numbers)

# Accessing elements using indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Tuple slicing
print("First three elements:", numbers[:3])
print("Elements from index 1 to 3:", numbers[1:4])

# Finding the length
print("Length of tuple:", len(numbers))

# Basic tuple operations
print("Tuple repetition:", numbers[:2] * 2)
print("Is 30 present?", 30 in numbers)

# Tuple concatenation
more_numbers = (60, 70)
combined = numbers + more_numbers
print("Combined tuple:", combined)

# Counting and finding an index
print("Count of 20:", numbers.count(20))
print("Index of 40:", numbers.index(40))
