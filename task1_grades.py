
try:
    marks = float(input("Enter student marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
    elif marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: Fail")

except ValueError:
    print("Invalid input! Please enter a number.")
