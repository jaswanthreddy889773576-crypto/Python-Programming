# Creating a class
class Employee:

    # Constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Method to display employee information
    def display(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Salary:", self.salary)
        print("----------------------")


# Creating objects with different values
employee1 = Employee("Rahul", 25, 30000)
employee2 = Employee("Arjun", 28, 45000)

# Displaying employee information
print("Employee Details")
employee1.display()
employee2.display()
