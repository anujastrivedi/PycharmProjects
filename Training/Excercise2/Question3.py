# Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all information of the student.
# 2. setAge - It should assign an age to student
# 3. setMarks - It should assign marks to the student.


class Student:
    def __init__(self, stud_name, roll_no):
        self.stud_name = stud_name
        self.roll_no = roll_no
        self.age = ""
        self.marks = []

    def set_age(self):
        self.age = 20

    def set_marks(self):
        self.marks = {"maths": 80, "english": 70, "finance": 85}

    def student_detail(self):
        self.set_age()
        self.set_marks()
        return f"Student Name : {self.stud_name} \nStudent Roll Number : {self.roll_no} \nStudent Age : {self.age} " \
               f"\nStudent Marks : {self.marks}"

    def __str__(self):
        return self.student_detail()


student = Student("Adam", 30)
print(student)
