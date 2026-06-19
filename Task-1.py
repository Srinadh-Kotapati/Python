
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


class Employee:
    def generate_id_card(self,Employee_ID,Employee_Name,Department,Salary):
        self.Employee_ID = Employee_ID
        self.Employee_Name=Employee_Name
        self.Department = Department
        self.Salary = Salary
    def display_id_card(self):
           print("Employee ID :", self.Employee_ID)
           print("Employee Name :", self.Employee_Name)
           print("Department :", self.Department)
           print("Salary :", self.Salary)
           print("           ")
        

emp1 = Employee()
emp1.generate_id_card(1, "Srinadh", "Python", 20000)
emp2 = Employee()
emp2.generate_id_card(2, "Shiva", "Python", 25000)
emp3 = Employee()
emp3.generate_id_card(3, "Pavan", "Python", 27000)
emp4 = Employee()
emp4.generate_id_card(4, "Uday", "Python", 28000)

print("Employee ID card")
emp1.display_id_card()

print("Employee ID card")
emp2.display_id_card()

print("Employee ID card")
emp3.display_id_card()

print("Employee ID card")
emp4.display_id_card()




class Product:
    def display_product(self,product_id,product_name,brand,price):
        self.product_id = product_id
        self.product_name = product_name
        self.brand = brand
        self.price = price
    def display_products(self):
        print("Product ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Brand        :", self.brand)
        print("Price        :", self.price)
        print(                       )
        

laptop = Product()
laptop.display_product(101, "Laptop", "Dell", 55000)
Mobile = Product()
Mobile.display_product(102, "Mobile", "Samsung", 25000)
keyboard = Product()
keyboard.display_product(103, "Keyboard", "Logitech", 1200)
Mouse = Product()
Mouse.display_product(104, "Mouse", "HP", 800)
Moniter = Product()
Moniter.display_product(105, "Monitor", "LG", 15000)

laptop.display_products()
Mobile.display_products()
keyboard.display_products()
Mouse.display_products()
Moniter.display_products()
print("Total Products Created : 5")




class BankCustomer:
    def display_customer(self,Account_Number,Customer_Name,Account_Type, Account_Balance):
        self.Account_Number = Account_Number
        self.Customer_Name = Customer_Name
        self.Account_Type = Account_Type
        self.Account_Balance = Account_Balance

    def check_balance(self):
        print("Customer Name : ", self.Customer_Name)
        print("Account Number: ",self.Account_Number)
        print("Account Type :",self.Account_Type)
        print("Balance :",self.Account_Balance)
        print(                        )

customer1 = BankCustomer()
customer1.display_customer(440802010008979, "Srinadh", "Savings", 2000)

customer2 = BankCustomer()
customer2.display_customer(73558353479,"Mahesh","Savings", 3500000)

customer3 = BankCustomer()
customer3.display_customer(58466398465674, "Tarak","Savings",100000000)

customer4 = BankCustomer()
customer4.display_customer(746840847758,"Prabhas","Savings",675674)

print("Customer Details")
customer1.check_balance()
customer2.check_balance()
customer3.check_balance()
customer4.check_balance()



class FoodOrder:
    def __init__(self,Order_ID,Customer_Name,Restaurant_Name,Food_Item,Quantity,Price_per_Item):
        self.Order_ID = Order_ID
        self.Customer_Name = Customer_Name
        self.Restaurant_Name = Restaurant_Name
        self.Food_Item = Food_Item
        self.Quantity= Quantity
        self.Price_per_Item = Price_per_Item
    

    def display_order(self):
        print("Order ID :      ", self.Order_ID )
        print("Customer Name :  ",self.Customer_Name)
        print("Restaurant Name :",self.Restaurant_Name)
        print("Food Item :     ", self.Food_Item)
        print("Quantity :      ", self.Quantity)
        print("Price per Item : ",self.Price_per_Item)
        

    
    def calculate_bill(self):
        return self.Quantity * self.Price_per_Item
        
print("Food Order Details")
Order1 = FoodOrder(1,"Srinadh","Bawarchi","Cicken curry",2,350)
Order1.display_order()
Bill = Order1.calculate_bill()
print("Total Bill :" ,Bill)
print(                        )

print("Food Order Details")
Order1 = FoodOrder(2,"shiva","chinthamani","Cicken Fry Biriyani",3,130)
Order1.display_order()
Bill = Order1.calculate_bill()
print("Total Bill :" ,Bill)
print(                        )

print("Food Order Details")
Order1 = FoodOrder(3,"Uday","Godavari Ruchulu","Fry biriyani",2,140)
Order1.display_order()
Bill = Order1.calculate_bill()
print("Total Bill :" ,Bill)
print(                        )

print("Food Order Details")
Order1 = FoodOrder(4,"Narasimha","Rajugari biriyani","Cicken biriyani",4,200)
Order1.display_order()
Bill = Order1.calculate_bill()
print("Total Bill :" ,Bill)
print(                        )

print("Food Order Details")
Order1 = FoodOrder(5,"Pavan","Bangarubabu biriyani","chicken dhum biriyani",3,350)
Order1.display_order()
Bill = Order1.calculate_bill()
print("Total Bill :" ,Bill)
print(                        )









 


