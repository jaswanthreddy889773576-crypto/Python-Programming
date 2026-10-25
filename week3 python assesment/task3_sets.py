# Creating a set and removing duplicates
numbers = {10, 20, 30, 20, 40, 10}
print("Original set:", numbers)

# Adding an element
numbers.add(50)
print("After adding 50:", numbers)

# Removing an element
numbers.remove(30)
print("After removing 30:", numbers)

# Safely removing an element
numbers.discard(100)
print("After discard:", numbers)

# Creating two sets
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

# Union
print("Union:", set_a.union(set_b))

# Intersection
print("Intersection:", set_a.intersection(set_b))

# Difference
print("Difference (A - B):", set_a.difference(set_b))
print("Difference (B - A):", set_b.difference(set_a))

# Membership testing
print("Is 20 in set A?", 20 in set_a)
