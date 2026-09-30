class Student:
    def __init__(self, roll, name, marks, address):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.address = address

    def display_student(self):
        print("Student Roll No:", self.roll)
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)
        print("Student Address:", self.address)


class Teacher:
    def __init__(self, name, salary, dep, address):
        self.name = name
        self.salary = salary
        self.dep = dep
        self.address = address

    def display_teacher(self):
        print("Teacher Name:", self.name)
        print("Teacher Salary:", self.salary)
        print("Teacher Department:", self.dep)
        print("Teacher Address:", self.address)


class College:
    def __init__(self, student, teacher):
        self.student = student
        self.teacher = teacher

    def display_college(self):
        print("----- Student Details -----")
        self.student.display_student()

        print("\n----- Teacher Details -----")
        self.teacher.display_teacher()


# Create Student object
s1 = Student(101, "Ashwini", 85, "Pune")

# Create Teacher object
t1 = Teacher("Atul Sir", 50000, "Computer", "Pune")

# Create College object
c1 = College(s1, t1)

# Display details
c1.display_college()
    

   
