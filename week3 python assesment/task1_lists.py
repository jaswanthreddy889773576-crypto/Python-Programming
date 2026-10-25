# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding an element
fruits.append("Grapes")
print("After adding:", fruits)

# Updating an element
fruits[1] = "Pineapple"
print("After updating:", fruits)

# Removing an element
fruits.remove("Mango")
print("After removing:", fruits)

# Sorting the list
fruits.sort()
print("Sorted list:", fruits)

# List slicing
print("First two fruits:", fruits[:2])