# Task 1: File Handling
# Objective: Create, write, read, and append data to a text file.
file_name = "student.txt"
# Step 1: Create a file and write data into it
with open(file_name, "w") as file:
    file.write("Student Name: jaswanth\n")
    file.write("Course: Python Programming\n")
    file.write("Week: 4 Internship\n")
print("Data written successfully.")
# Step 2: Read and display the file content
print("\nOriginal File Content:")
with open(file_name, "r") as file:
    content = file.read()
    print(content)
# Step 3: Append new data to the existing file
with open(file_name, "a") as file:
    file.write("Status: In Progress\n")
print("New data appended successfully.")
# Step 4: Display the updated file content
print("\nUpdated File Content:")
with open(file_name, "r") as file:
    updated_content = file.read()
    print(updated_content)