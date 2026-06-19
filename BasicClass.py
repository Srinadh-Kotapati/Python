'''
      1. Classes & Objects
Problem 1: Student Management

Create a Student class with:

name
roll number
marks in 3 subjects

Methods:

calculate average
calculate grade
display student details

Extra:

Create multiple student objects.
'''

class Student:
    def __init__(self,name,roll_number,sub1,sub2,sub3):
        self.name = name
        self.roll_number = roll_number
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    def calling(self):
        avg = (self.sub1+self.sub2+self.sub3)/3
        print(avg)
obj = Student("srinadh",23,97,98,99)
obj.calling()


class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        self.avg = 0
        self.sub1 = 0
        self.sub2 = 0
        self.sub3 = 0
    def calling(self):
        sub1 = int(input("Enter subject 1 marks:"))
        sub2= int(input("Enter subject 2 marks:"))
        sub3 = int(input("Enter subject 3 marks:"))
        self.avg = (sub1+sub2+sub3)/3
        print(self.avg)
    def grade(self):
        obj = Student("srinadh",23)
obj.calling()


class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.avg = 0

    def grade(self, marks):
        if marks >= 90:
            return "A+"
        elif marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "Fail"

    def calling(self):
        self.sub1 = int(input("Enter subject 1 marks: "))
        self.sub2 = int(input("Enter subject 2 marks: "))
        self.sub3 = int(input("Enter subject 3 marks: "))

        self.avg = (self.sub1 + self.sub2 + self.sub3) / 3

        print("Subject 1 Grade:", self.grade(self.sub1))
        print("Subject 2 Grade:", self.grade(self.sub2))
        print("Subject 3 Grade:", self.grade(self.sub3))
        print("Average:", self.avg)


obj = Student("srinadh", 23)
obj.calling()


'''

Problem 3: Rectangle Calculator

Create a Rectangle class.

Methods:

area()
perimeter()

Create different rectangle objects.
'''


class rectangle:
    
    def __init__(self):
    
        self.l = 0
        self.w = 0
        self.area = 0
        self.perimeter = 0
        
    def Area(self):
        self.l = int(input("Enter length of rectangle:"))
        self.w = int(input("Enter width of rectangle:")) 
        self.area = self.l * self.w
        print(self.area)
    def Perimeter(self):
        self.perimeter = 2*(self.l+self.w)
        print(self.perimeter)
obj = rectangle()
obj.Area()
obj.Perimeter()






