# Creating a student information dictionary
student = {
    "Name": "Rahul",
    "Age": 20,
    "Course": "Python Programming",
    "City": "Tirupati"
}

print("Student Information:", student)

# Accessing values
print("Name:", student["Name"])
print("Age:", student.get("Age"))

# Adding a new key-value pair
student["Email"] = "rahul@example.com"
print("After adding Email:", student)

# Updating a value
student["Age"] = 21
print("After updating Age:", student)

# Removing data
student.pop("City")
print("After removing City:", student)

# Displaying keys and values
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Checking whether a key exists
print("Is Course present?", "Course" in student)

# Displaying details using a loop
print("Final Student Details:")
for key, value in student.items():
    print(key, ":", value)

# Finding the number of details
print("Number of details:", len(student))
