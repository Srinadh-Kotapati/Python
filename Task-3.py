'''
class Student:
 
    Institute_Name = "ABC Training Institute"
    
    def __init__(self,Student_ID,Student_Name,Course):
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.Course = Course

    def display_student(self):
        print("Student ID :",self.Student_ID)
        print("Student Name :",self.Student_Name)
        print("Course :",self.Course)

    
print("Student Details   ")
Student1 = Student(20,"Vicky","CSE")
print(Student1.Institute_Name)
Student1.display_student()
print(                      )


Student2 = Student(21,"Kathrina","ECE")
print(Student2.Institute_Name)
Student2.display_student()
print(                      )


Student3 = Student(22,"Ranbir","AIML")
print(Student3.Institute_Name)
Student3.display_student()
print(                      )


Student4 = Student(23,"Kiara","AIDS")
print(Student4.Institute_Name)
Student4.display_student()
print(                      )


Student5 = Student(24,"Vikram","IT")
print(Student5.Institute_Name)
Student5.display_student()
print(                      )


class Employee:

    Company_Name = "Tech Solutions Pvt Ltd"

    def __init__(self,Employee_ID,Employee_Name,Department,Salary):
        self.Employee_ID = Employee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.Salary = Salary

    def display_employee(self):
        print("Employee Id :",self.Employee_ID)
        print("Employee Name :",self.Employee_Name)
        print("Department :",self.Department)
        print("Salary :",self.Salary)
        
    def Bonus(self):
        Bonus = 5000
        return self.Salary + Bonus
    
print("Employee Details   ")
print(                  )
Employee1 = Employee("E1001","Vijay","SAP",55000)
print(Employee1.Company_Name)
Employee1.display_employee()
Total_Salary = Employee1.Bonus()    
print("Bonus :",Total_Salary)

Employee2 = Employee("E1002","Surya","Salesforce",75000)
print(Employee1.Company_Name)
Employee2.display_employee()
Total_Salary = Employee2.Bonus()    
print("Bonus :",Total_Salary)
print(                  )

Employee3 = Employee("E1003","Vikram","ServiceNow",45000)
print(Employee1.Company_Name)
Employee3.display_employee()
Total_Salary = Employee3.Bonus()    
print("Bonus :",Total_Salary)
print(                  )

Employee4 = Employee("E1004","Karthik","Python",65000)
print(Employee1.Company_Name)
Employee4.display_employee()
Total_Salary = Employee4.Bonus()    
print("Bonus :",Total_Salary)
print(                  )



class Customer:

    BANK_NAME = "Natioanl Bank of India"

    def __init__(self,Account_Number,Customer_Name,Account_Type,Balance):
        self.Account_Number = Account_Number
        self.Customer_Name = Customer_Name
        self.Account_Type = Account_Type
        self.Balance = Balance

    def display_account(self):
        print("Account Number :",self.Account_Number)
        print("Customer Name :",self.Customer_Name)
        print("Account Type :",self.Account_Type)
        print("Balance :",self.Balance)


Customer1 = Customer(53655436,"Rajmouli","Savings",5000000)
print("Bank Name :", Customer1.BANK_NAME)
Customer1.display_account()
print(                       )


Customer2 = Customer(84649838,"Sandeep R Vanga","Savings",70000)
print("Bank Name :", Customer2.BANK_NAME)
Customer2.display_account()
print(                       )

Customer3 = Customer(776573898,"Puri","Savings",80000)
print("Bank Name :", Customer3.BANK_NAME)
Customer3.display_account()
print(                       )


Customer4 = Customer(96367483,"sukku","Savings",10000)
print("Bank Name :", Customer4.BANK_NAME)
Customer4.display_account()
print(                       )


Customer5 = Customer(6478494,"Prasanth Neel","Savings",10000000)
print("Bank Name :", Customer5.BANK_NAME)
Customer5.display_account()
print(                       )


class Product:

    GST = "18%"

    def __init__(self,Product_ID,Product_Name,Brand,Price):
        self.Product_ID = Product_ID
        self.Product_Name = Product_Name
        self.Brand = Brand
        self.Price = Price

    def display_product(self):
        print("Product ID :",self.Product_ID)
        print("Product Name :",self.Product_Name)
        print("Brand :",self.Brand)
        print("Price :",self.Price)
    
    def Other_Details(self):
        return "10%"
    
print("Product Details ")
Product1 = Product("GT63","T-shirt","U.S POLO",2700)
Product1.display_product()
print("GST :",Product1.GST)
print("DISCOUNT :",Product1.Other_Details())
print(                           )

print("Product Details ")
Product2 = Product("MH43","Full sleves","U.S POLO",1700)
Product2.display_product()
print("GST :",Product2.GST)
print("DISCOUNT :",Product2.Other_Details())
print(                           )

print("Product Details ")
Product3 = Product("H247","Jeans Pant","Spykar",3700)
Product3.display_product()
print("GST :",Product3.GST)
print("DISCOUNT :",Product3.Other_Details())
print(                           )

print("Product Details ")
Product4 = Product("K65","Chinos","Net Play",1700)
Product4.display_product()
print("GST :",Product4.GST)
print("DISCOUNT :",Product4.Other_Details())
print(                           )

print("Product Details ")
Product5 = Product("J45","Shirt","U.S POLO",2700)
Product5.display_product()
print("GST :",Product5.GST)
print("DISCOUNT :",Product5.Other_Details())
print(                           )
'''


HOSPITAL_NAME = "City Care Hospital"
class Patient:

    Doctor_Name = "Dr.Sharma"
    
    def __init__(self,Patient_ID,Patient_Name,Age,Disease,Consultation_Fee):
        self.Patient_ID = Patient_ID
        self.Patient_Name = Patient_Name
        self.Age = Age
        self.Disease = Disease
        self.Consultation_Fee = Consultation_Fee

    def display_patient(self):
        print("Patient ID  :",self.Patient_ID)
        print("Patient Name :",self.Patient_Name)
        print("Age :",self.Age)
        print("Disease :",self.Disease)
        self.Room_Charge = "Rs.1000"
       

    def display_hospital(self):
        print("Consultation Fee :",self.Consultation_Fee)
        

print("Hospital Details   ")
print(                          )
print("Hospital Name :",HOSPITAL_NAME)
Patient1 = Patient("P101","Kohli",40,"Fever",700)
print("Doctor Name :",Patient1.Doctor_Name) 
Patient1.display_patient()
print(                         )
Patient1.display_hospital()
print("Room Charge :",Patient1.Room_Charge)

print(                          )
print("Hospital Name :",HOSPITAL_NAME)
Patient2 = Patient("P102","Dhoni",43,"Cramps",700)
print("Doctor Name :",Patient2.Doctor_Name) 
Patient2.display_patient()
print(                         )
Patient2.display_hospital()
print("Room Charge :",Patient2.Room_Charge)

print(                          )
print("Hospital Name :",HOSPITAL_NAME)
Patient3 = Patient("P103","KL Rahul",35,"Injury",700)
print("Doctor Name :",Patient3.Doctor_Name) 
Patient3.display_patient()
print(                         )
Patient3.display_hospital()
print("Room Charge :",Patient3.Room_Charge)

print(                          )
print("Hospital Name :",HOSPITAL_NAME)
Patient4 = Patient("P104","Iyer",32,"Fever",800)
print("Doctor Name :",Patient4.Doctor_Name) 
Patient4.display_patient()
print(                         )
Patient4.display_hospital()
print("Room Charge :",Patient4.Room_Charge)

print(                          )
print("Hospital Name :",HOSPITAL_NAME)
Patient5 = Patient("P105","Ruturaj",29,"Cough",700)
print("Doctor Name :",Patient5.Doctor_Name) 
Patient5.display_patient()
print(                         )
Patient5.display_hospital()
print("Room Charge :",Patient5.Room_Charge)

        





        



        




        


        



        
