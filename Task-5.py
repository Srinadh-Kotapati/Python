'''
class Student:

    def __init__(self,Student_ID,Student_Name):
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.__Marks = 0

    def set_marks(self,Marks):
        self.__Marks = Marks

    def get_marks(self):
        return self.__Marks
    
    def display_student(self):
        print("Student Details")
        print("Student ID :", self.Student_ID)
        print("Student Name :",self.Student_Name)
        print("Marks :",self.get_marks())

s1 = Student(101,"Zaheer Khan")
s2= Student(102,"Anil")
s3 = Student(103,"Rahul")
s4 = Student(104,"Irfan")
s5 = Student(105,"Nehra")
s1.set_marks(85)
s2.set_marks(92)
s3.set_marks(76)
s4.set_marks(87)
s5.set_marks(86)

s1.display_student()
print()
s2.display_student()
print()
s3.display_student()
print()
s4.display_student()
print()
s5.display_student()


class BankAccount:
    def __init__(self,Account_Number,Customer_Name,Balance):
        self.Account_Number = Account_Number
        self.Customer_Name = Customer_Name
        self.__Balance = Balance

    def deposit(self,amount):
        self.__Balance += amount
        print(amount,"Deposited Successfully")

    def withdraw(self,amount):
        self.__Balance -= amount
        print(amount,"withdraw successfull")

    def get_balance(self):
        return self.__Balance
    
    def display_customer(self):
        print("Customer Details")
        print("Customer Name :",self.Customer_Name)
        print("Account Number :",self.Account_Number)
        print(               )
        print("Available Balance :",self.get_balance())

BA1 = BankAccount(73573837638,"Ishan",5000)
BA2 = BankAccount(6735537373,"Parsidh",7000)
BA3 = BankAccount(738783636,"Prince",8677)

BA1.display_customer()
print()
BA1.deposit(670)
BA1.display_customer()
print()
BA1.withdraw(30)
BA1.display_customer()
print()
print("--------------------------------------------------------------")
BA2.display_customer()
print()
BA2.deposit(6790)
BA2.display_customer()
print()
BA2.withdraw(350)
BA2.display_customer()
print()
print("-----------------------------------------------------------------")
BA3.display_customer()
print()
BA3.deposit(870)
BA3.display_customer()
print()
BA3.withdraw(480)
BA3.display_customer()
print()



class Employee:
    def __init__(self,Employee_ID,Employee_Name,Department):
        self.Employee_ID = Employee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.__Salary = 0

    def set_salary(self,Salary):
    
        if isinstance(Salary, (int, float)) and Salary >= 15000:
            self.__Salary = Salary
        else:
            print("Invalid Salary")
    
    def get_salary(self):
        return self.__Salary
    
    def display_employee(self):
        print("Employee Details")
        print("Employee ID :",self.Employee_ID)
        print("Employee Name :",self.Employee_Name)
        print("Department :",self.Department)
        print()

        if self.__Salary == 0:
         print("Salary : Invalid Salary")
        else:
         print("Salary :", self.__Salary)

E1 = Employee(101,"Srinadh","Python")
E2 = Employee(102,"SHIVA","Java")
E3 = Employee(103,"Pavan","Cloud")
E4 = Employee(104,"Uday","SAP")
E5 = Employee(105,"Narasimha","AI ")

E1.set_salary(17800)
E1.display_employee()
print()

E2.set_salary(8000)
E2.display_employee()
print()

E3.set_salary("Hello")
E3.display_employee()
print()

E4.set_salary(20000)
E4.display_employee()
print()

E5.set_salary(15000)
E5.display_employee()
print()


class CustomerWallet:
    def __init__(self,Customer_ID,Customer_Name,Wallet_Balance):
        self.Customer_ID = Customer_ID
        self.Customer_Name = Customer_Name
        self.__Wallet_Balance = Wallet_Balance

    def add_money(self,amount):
        if amount <= 0:
            print("Please add money")
        else:
         self.__Wallet_Balance += amount
         print(amount,"Added successfully")

    def purchase(self,amount):
        if amount <= 0 :
            print("Purchase amount must be positive")
        else:
         self.__Wallet_Balance -= amount
         print(f"Purchase successfull and spent {amount}")

    def check_balance(self):
        return self.__Wallet_Balance
    
    def display_customer(self):
        print("Wallet Details")
        print(          )
        print("Customer ID :",self.Customer_ID)
        print("Customer Name :",self.Customer_Name)
        print()
        print("Check Balance : ",self.check_balance())

CWD1 = CustomerWallet(1,"Srinadh",5000)
print()
CWD1.display_customer()
CWD1.add_money(5000)
print("----------------------------------")
CWD1.display_customer()
print()
CWD1.purchase(2000)
print("-----------------------------------")
CWD1.display_customer()

print("-------------------------------------------------------------------")
CWD2 = CustomerWallet(2,"vijay",15000)
print()
CWD2.display_customer()
CWD2.add_money(7000)
print("----------------------------------")
CWD2.display_customer()
print()
CWD2.purchase(20000)
print("-----------------------------------")
CWD2.display_customer()

print("---------------------------------------------------------------")
CWD3 = CustomerWallet(3,"Murali",6750)
print()
CWD3.display_customer()
CWD3.add_money(1250)
print("----------------------------------")
CWD3.display_customer()
print()
CWD3.purchase(6800)
print("-----------------------------------")
CWD3.display_customer()

print("----------------------------------------------------------------------")

CWD4 = CustomerWallet(4,"Dinesh",25000)
print()
CWD4.display_customer()
CWD4.add_money(3000)
print("----------------------------------")
CWD4.display_customer()
print()
CWD4.purchase(22000)
print("-----------------------------------")
CWD4.display_customer()

print("-----------------------------------------------------------------")
CWD5 = CustomerWallet(5,"Karthik",30000)
print()
CWD5.display_customer()
CWD5.add_money(2000)
print("----------------------------------")
CWD5.display_customer()
print()
CWD5.purchase(2000)
print("-----------------------------------")
CWD5.display_customer()

print("------------------------------------------------------------------------")
'''

class Patient:
    def __init__(self,Patient_ID,Patient_Name,Age,Disease):
        self.Patient_ID = Patient_ID
        self.Patient_Name = Patient_Name
        self.Age = Age
        self.Disease = Disease

    def set_medical_history(self,Medical_History):
        self.__Medical_History = Medical_History
    
    def get_medical_history(self):
        return self.__Medical_History
    
    def __calculate_discount(self):
        if self.__Consultation_Fee > 1000:
            return self.__Consultation_Fee * 0.10
        else:
            return 0
    
    def final_bill(self, Consultation_Fee):
        self.__Consultation_Fee = Consultation_Fee
        discount = self.__calculate_discount()
        return self.__Consultation_Fee - discount
    
    
    def display_patient(self):
        print("Patient Details")
        print(                 )
        print("Patient ID :",self.Patient_ID)
        print("Patient Name :",self.Patient_Name)
        print("Age :", self.Age)
        print("Disease :",self.Disease)
        print()
        print("Medical History :",self.get_medical_history())
        print("Consultation Fee : ", self.__Consultation_Fee)
        print("Discount : ", self.__calculate_discount())
        print("Final Bill : ", self.final_bill(self.__Consultation_Fee))

P1 = Patient("P101","Srinadh",23,"Fever")
P2 = Patient("P102","Vaibhav",16,"Cardiac")
P3 = Patient("P103","Priyansh",22,"Injury")
P4 = Patient("P104","Ruturaj",29,"Cold")
P5 = Patient("P105","Tilak",28,"Fever")

P1.set_medical_history("Cough")
P1.final_bill(1170)
P1.display_patient()

P2.set_medical_history("Body pains")
P2.final_bill(1700)
P2.display_patient()

P3.set_medical_history("Cough")
P3.final_bill(1550)
P3.display_patient()

P4.set_medical_history("Cough")
P4.final_bill(1300)
P4.display_patient()

P5.set_medical_history("Cough")
P5.final_bill(1800)
P5.display_patient()


        
        






    

        





        

    









        

    

        
