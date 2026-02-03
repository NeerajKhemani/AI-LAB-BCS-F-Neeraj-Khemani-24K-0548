#Task 3: Student Result System
#Design a Student Result System using encapsulation.
#Requirements:
#1. Private attribute __marks
#2. Methods: set_marks(), get_marks(), calculate_grade()
#3. Create at least two student objects

#Neeraj Khemani 24K-0548
class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0   

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def calculate_grade(self):
        if self.__marks >= 86:
            return "A"
        elif self.__marks >= 72:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "F"


s1 = Student("Faiz")
s1.set_marks(88)
print(f"Name: {s1.name} \nMarks: {s1.get_marks()} \nGrade: {s1.calculate_grade()}")

s2 = Student("Altaf")
s2.set_marks(72)
print(f"\nName: {s2.name} \nMarks: {s2.get_marks()} \nGrade: {s2.calculate_grade()}")
