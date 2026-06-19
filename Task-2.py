
class Student:
    def __init__(self,Student_ID,Student_Name,Course,Course_Fee):
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.Course = Course
        self.Course_Fee = Course_Fee
    
    def display_student(self):
        print("Student ID :", self.Student_ID)
        print("Student Name :", self.Student_Name)
        print("Course :",self.Course)
        print("Course Fee :", self.Course_Fee)
        print(                           )

print("Student Details")
Student1 = Student(1,"Srinadh","Python Full-Stack",25000)
Student1.display_student()

Student2 = Student(2,"Pavan","Python Full-Stack",25000)
Student2.display_student()

Student3 = Student(1,"Uday","Python Full-Stack",25000)
Student3.display_student()

Student4 = Student(4,"Narasimha","Python Full-Stack",25000)
Student4.display_student()



class Employee:
    def __init__(self,Emploee_ID,Employee_Name,Department,Salary):
        self.Employee_ID = Emploee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.Salary = Salary

    def display_Employee(self):
        print("Employee ID :", self.Employee_ID)
        print("Employee Name :",self.Employee_Name)
        print("Department :", self.Department)
        print("Salary :", self.Salary)
    
    def annual_salary(self):
        return self.Salary * 12
    
print("Employee Details   ")    
Employee1 = Employee(1,"Srinadh","Python",20000)
Employee1.display_Employee()
Total_Salary = Employee1.annual_salary()
print("Annaul Salary :", Total_Salary)
print(                             )

Employee2 = Employee(2,"Shiva","Python",21000)
Employee2.display_Employee()
Total_Salary = Employee2.annual_salary()
print("Annual Salary :", Total_Salary)
print(                             )


Employee3 = Employee(3,"Pavan","Python",22000)
Employee3.display_Employee()
Total_Salary = Employee3.annual_salary()
print("Annual Salary :", Total_Salary)
print(                             )


Employee4 = Employee(4,"Uday","Python",23000)
Employee4.display_Employee()
Total_Salary = Employee4.annual_salary()
print("Annual Salary :", Total_Salary)
print(                             )


Employee5 = Employee(5,"Narasimha","Python",24000)
Employee5.display_Employee()
Total_Salary = Employee5.annual_salary()
print("Annual Salary :", Total_Salary)
print(                             )




class Order:
    def __init__(self,Order_ID,Customer_Name,Product_Name,Quantity,Price_per_Item):
        self.Order_ID = Order_ID
        self.Customer_Name = Customer_Name
        self.Product_Name = Product_Name
        self.Quantity = Quantity
        self.Price_per_Item = Price_per_Item

    def display_order(self):
        print("Order ID :",self.Order_ID)
        print("Customer Name :",self.Customer_Name)
        print("Product Name :",self.Product_Name)
        print("Quantity :",self.Quantity)
        print("Price per Item :",self.Price_per_Item)
    
    def calculate_total(self):
        return self.Quantity * self.Price_per_Item
    
print("Order Details   ")    
Order1 = Order("p101","Srinadh","Printed T-shirt",2,450)
Order1.display_order()
Total_Amount = Order1.calculate_total()
print("Total Amount :", Total_Amount)
print(                                 )

Order2 = Order("p102","Vamsi","Checks Shirt",3,4550)
Order2.display_order()
Total_Amount = Order2.calculate_total()
print("Total Amount :", Total_Amount)
print(                                 )

Order3 = Order("p103","Vijay","T-shirt",2,750)
Order3.display_order()
Total_Amount = Order3.calculate_total()
print("Total Amount :", Total_Amount)
print(                                 )

Order4 = Order("p104","Tarak","Jeans Pant",1,2350)
Order4.display_order()
Total_Amount = Order4.calculate_total()
print("Total Amount :", Total_Amount)
print(                                 )

Order5 = Order("p105","vara","chinos",4,550)
Order5.display_order()
Total_Amount = Order5.calculate_total()
print("Total Amount :", Total_Amount)
print(                                 )




class Patient:
    def __init__(self,Patient_ID,Patient_Name,Age,Disease,Consultation_Fee):
        self.Patient_ID = Patient_ID
        self.Patient_Name = Patient_Name
        self.Age = Age
        self.Disease = Disease
        self.Consultation_Fee = Consultation_Fee

    def display_patient(self):
        print("Patient ID :",self.Patient_ID)
        print("Patient Name :",self.Patient_Name)
        print("Age :",self.Age)
        print("Disease :",self.Disease)
        #print("Consultation Fee :",self.Consultation_Fee)

    def display_fee(self):
        return self.Consultation_Fee
    
print("Patient Details   ")    
Patient1 = Patient(1,"Prabhas",50,"Viral Fever",500)
Patient1.display_patient()
Fee = Patient1.display_fee()
print("Cosultation Fee :", Fee)
print(                       )

Patient2 = Patient(2,"Ram Charan",45,"Cancer",1000)
Patient2.display_patient()
Fee = Patient2.display_fee()
print("Cosultation Fee :", Fee)
print(                       )

Patient3 = Patient(3,"Pawan Kalyan",55,"Body Pains",600)
Patient3.display_patient()
Fee = Patient3.display_fee()
print("Cosultation Fee :", Fee)
print(                       )

Patient4 = Patient(4,"Allu Arjun",40,"Injury",700)
Patient4.display_patient()
Fee = Patient4.display_fee()
print("Cosultation Fee :", Fee)
print(                       )

Patient5 = Patient(5,"Chiru",65,"Cnacer",1500)
Patient5.display_patient()
Fee = Patient5.display_fee()
print("Cosultation Fee :", Fee)
print(                       )



class HotelBooking:
    def __init__(self,Booking_ID,Customer_Name,Room_Type,Number_of_Days,Rent_Per_Day):
        self.Booking_ID = Booking_ID
        self.Customer_Name = Customer_Name
        self.Room_Type = Room_Type
        self.Number_of_Days = Number_of_Days
        self.Rent_Per_Day = Rent_Per_Day

    def display_Booking(self):
        print("Booking ID :",self.Booking_ID)
        print("Customer Name :",self.Customer_Name)
        print("Room Type :",self.Room_Type)
        print("Number of Days :",self.Number_of_Days)
        print("Rent Per Days :",self.Rent_Per_Day)

    def calculate_Bill(self):
        return self.Number_of_Days * self.Rent_Per_Day
    
print("Booking Details    ")
Customer1 = HotelBooking("R101","Ben","Luxury",2,3000)
Customer1.display_Booking()
Total_Bill = Customer1.calculate_Bill()
print("Total Bill :",Total_Bill)
print(                       )

Customer2 = HotelBooking("R102","Benjamen","Ordinary",3,1500)
Customer2.display_Booking()
Total_Bill = Customer2.calculate_Bill()
print("Total Bill :",Total_Bill)
print(                       )


Customer3 = HotelBooking("R103","Denver","Premium",2,2000)
Customer3.display_Booking()
Total_Bill = Customer3.calculate_Bill()
print("Total Bill :",Total_Bill)
print(                       )


Customer4 = HotelBooking("R104","Tokyo","Ordinary",5,1000)
Customer4.display_Booking()
Total_Bill = Customer4.calculate_Bill()
print("Total Bill :",Total_Bill)
print(                       )


Customer5 = HotelBooking("R105","Nick","Luxury",2,3000)
Customer5.display_Booking()
Total_Bill = Customer5.calculate_Bill()
print("Total Bill :",Total_Bill)
print(                       )



        




        
        




        


