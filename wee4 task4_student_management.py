
# Week 4 - Task 4: Student Management System
# Mini Python Project
# Concepts: Variables, conditions, loops, functions, lists,
# dictionaries, file handling, exception handling, and libraries.

import json
import os
import random
from datetime import datetime

FILE_NAME = "students.json"


# Load student records from the file
def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print("Error: Invalid student data format.")
        return []

    except (json.JSONDecodeError, OSError) as error:
        print("Error loading student records:", error)
        return []


# Save student records to the file
def save_students(students):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        print("Records saved successfully.")

    except OSError as error:
        print("Error saving student records:", error)


# Add a new student
def add_student(students):
    print("\n--- Add Student ---")

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(s["id"] == student_id for s in students):
        print("Error: Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter age: "))
        if age <= 0 or age > 120:
            print("Error: Enter a valid age.")
            return

        course = input("Enter course: ").strip()
        if not course:
            print("Course cannot be empty.")
            return

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "created_at": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        students.append(student)
        save_students(students)
        print("Student added successfully!")

    except ValueError:
        print("Error: Age must be a valid integer.")


# Display all students
def view_students(students):
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-" * 35)
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Added On:", student.get("created_at", "Unknown"))

    print("-" * 35)


# Search for a student
def search_student(students):
    print("\n--- Search Student ---")
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found.")


# Update a student
def update_student(students):
    print("\n--- Update Student ---")
    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            new_name = input(
                "Enter new name (press Enter to keep current): "
            ).strip()

            new_age = input(
                "Enter new age (press Enter to keep current): "
            ).strip()

            new_course = input(
                "Enter new course (press Enter to keep current): "
            ).strip()

            if new_name:
                student["name"] = new_name

            if new_age:
                try:
                    age = int(new_age)
                    if age <= 0 or age > 120:
                        print("Error: Invalid age.")
                        return
                    student["age"] = age
                except ValueError:
                    print("Error: Age must be an integer.")
                    return

            if new_course:
                student["course"] = new_course

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete a student
def delete_student(students):
    print("\n--- Delete Student ---")
    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Generate a random student ID suggestion
def suggest_id(students):
    print("\n--- Random Student ID ---")

    while True:
        new_id = "STU" + str(random.randint(1000, 9999))

        if not any(s["id"] == new_id for s in students):
            print("Suggested student ID:", new_id)
            return


# Main menu
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Suggest Random Student ID")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            suggest_id(students)
        elif choice == "7":
            print("Thank you for using the Student Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


# Run the application
if __name__ == "__main__":
    main()
