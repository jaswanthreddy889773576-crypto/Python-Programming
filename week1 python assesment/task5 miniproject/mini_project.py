# Student Information Program

print("===== Student Information =====")

name = input("Enter student name: ")
age = int(input("Enter student age: "))
city = input("Enter city: ")
course = input("Enter course name: ")
marks = float(input("Enter marks: "))

print("\n===== Student Details =====")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)
print("Marks:", marks)

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)