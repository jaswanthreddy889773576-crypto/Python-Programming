
# Creating a class
class Student:

    # Method to display student information
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)
        print("----------------------")


# Creating first object
student1 = Student()
student1.name = "Rahul"
student1.age = 20
student1.course = "Python Programming"

# Creating second object
student2 = Student()
student2.name = "Arjun"
student2.age = 21
student2.course = "Data Science"

# Displaying information
print("Student Details")
student1.display()
student2.display()
