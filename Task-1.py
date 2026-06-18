'''
class Student:
    def display_details(self,Student_ID,Student_Name,Course_Name):
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.Course_Name = Course_Name
        return {
            "Student_ID":self.Student_ID,
              "Student_Name":self.Student_Name, 
              "Course_Name":self.Course_Name
                }                                                 #imp

obj = Student()
print("Student Details")
print(obj.display_details(1, "Srinadh", "Python Full-Stack" ))
print(obj.display_details(2, "shiva", "java Full-Stack" ))
print(obj.display_details(3, "pavan", "Python Full-Stack" ))
'''

class Employee:
    def generate_id_card(self,Employee_ID,Employee_Name,Department,Salary):
        self.Employee_ID = Employee_ID
        self.Employee_Name=Employee_Name
        self.Department = Department
        self.Salary = Salary
        return {
            "Employee ID"  :self.Employee_ID,
            "Employee Name"   : self.Employee_Name,
            "Department" : self.Department,
            "Salary" : self.Salary
            }

obj = Employee()
print("EMPLOYEE ID CARD")
print(obj.generate_id_card(1, "Srinadh", "Python", 20000))
print("EMPLOYEE ID CARD")
print(obj.generate_id_card(2, "Shiva", "Python", 25000))
print("EMPLOYEE ID CARD")
print(obj.generate_id_card(3, "Pavan", "Python", 27000))
print("EMPLOYEE ID CARD")
print(obj.generate_id_card(4, "Uday", "Python", 28000))
   






