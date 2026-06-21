from abc import ABC,abstractmethod
'''
class Payment(ABC):

    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def payment_status(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self,amount):
        self.amount = amount
    
    def make_payment(self):
        return f"Payment of Rs.{self.amount} has done using Credit Card Payment"
    
    def payment_status(self):
        return "Payment Successfull"

class DebitCardPayment(Payment):
    def __init__(self,amount):
        self.amount = amount
    
    def make_payment(self):
        return f"Payment of Rs.{self.amount} has done using Debit Card Payment"
    
    def payment_status(self):
        return "Payment Successfull"
    
class UpiPayment(Payment):
    def __init__(self,amount):
        self.amount = amount
    
    def make_payment(self):
        return f"Payment of Rs.{self.amount} has done using Upi Payment Method"
    
    def payment_status(self):
        return "Payment Successfull"
    
P1 = CreditCardPayment(5000)
P2 = DebitCardPayment(7600)
P3 = UpiPayment(7000)

print("Payment Details")
print(            )
print("Payment Method :",P1.make_payment())
print("Payment Status :",P1.payment_status())

print(            )
print("Payment Method :",P2.make_payment())
print("Payment Status :",P2.payment_status())

print(            )
print("Payment Method :",P3.make_payment())
print("Payment Status :",P3.payment_status())


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def working_hours(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,salary,Working_Hours):
        self.salary = salary
        self.Working_Hours = Working_Hours

    def calculate_salary(self):
        print("Employee Type : Full-Time")
        print("salary :",self.salary)
    
    def working_hours(self):
        print("workinh hours :",self.Working_Hours)
    
class PartTimeEmployee(Employee):
    def __init__(self,salary,Working_Hours):
        self.salary = salary
        self.Working_Hours = Working_Hours

    def calculate_salary(self):
        print("Employee Type : Part-Time")
        print("salary : ",self.salary)
    
    def working_hours(self):
        print("working hours :", self.Working_Hours)

class ContractEmployee(Employee):
    def __init__(self,salary,Working_Hours):
        self.salary = salary
        self.Working_Hours = Working_Hours

    def calculate_salary(self):
        print("Employee Type : Contract Type")
        print("salary :",self.salary)
    
    def working_hours(self):
        print("Working hours :",self.Working_Hours)
    
E1 = FullTimeEmployee(25000,9)
print("Employee Details")
E1.calculate_salary()
E1.working_hours()
print()

E2 = PartTimeEmployee(16000,5)
print("Employee Details")
E2.calculate_salary()
E2.working_hours()
print()

E3 = ContractEmployee(28000,10)
print("Employee Details")
E3.calculate_salary()
E3.working_hours()


class Restaurant(ABC):

    @abstractmethod
    def prepare_food(self):
        pass

    @abstractmethod
    def delivery_time(self):
        pass

    @abstractmethod
    def restaurant_details(self):
        pass

class Dominos(Restaurant):
    def __init__(self,Restaurant_Name,Food,Preparation_Time,Delivery_Time):
        self.Restaurant_Name = Restaurant_Name
        self.Food = Food
        self.Preparation_Time = Preparation_Time
        self.Delivery_Time = Delivery_Time

    def prepare_food(self):
        print(f"Preparation Time :,{self.Preparation_Time}min")
    
    def delivery_time(self):
        print(f"Delivery Time : {self.Delivery_Time}min")

    def restaurant_details(self):
        print("Restaurant Details")
        print()
        print("Restaurant Name :",self.Restaurant_Name)
        print("Food :",self.Food)


class KFC(Restaurant):
    def __init__(self,Restaurant_Name,Food,Preparation_Time,Delivery_Time):
        self.Restaurant_Name = Restaurant_Name
        self.Food = Food
        self.Preparation_Time = Preparation_Time
        self.Delivery_Time = Delivery_Time

    def prepare_food(self):
        print("Preparation Time :",self.Preparation_Time)
    
    def delivery_time(self):
        print("Delivery Time :",self.Delivery_Time)

    def restaurant_details(self):
        print("Restaurant Details")
        print()
        print("Restaurant Name :",self.Restaurant_Name)
        print("Food :",self.Food)


class Paradise(Restaurant):
    def __init__(self,Restaurant_Name,Food,Preparation_Time,Delivery_Time):
        self.Restaurant_Name = Restaurant_Name
        self.Food = Food
        self.Preparation_Time = Preparation_Time
        self.Delivery_Time = Delivery_Time

    def prepare_food(self):
        print("Preparation Time :",self.Preparation_Time)
    
    def delivery_time(self):
        print("Delivery Time :",self.Delivery_Time)

    def restaurant_details(self):
        print("Restaurant Details")
        print()
        print("Restaurant Name :",self.Restaurant_Name)
        print("Food :",self.Food)

RD1 = Dominos("Dominos","Pizza",25,15)
RD1.restaurant_details()
RD1.prepare_food()
RD1.delivery_time()
print()

RD2 = KFC("KFC","Fried Chicken",35,5)
RD2.restaurant_details()
RD2.prepare_food()
RD2.delivery_time()
print()

RD3 = Paradise(Paradise,"Chicken Biriyani",10,25)
RD3.restaurant_details()
RD3.prepare_food()
RD3.delivery_time()


class Vehicle(ABC):

    @abstractmethod
    def rental_price(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def vehicle_details(self):
        pass

class Bike(Vehicle):
    def __init__(self,charge,fuel,details):
        self.charge = charge
        self.fuel = fuel
        self.details = details

    def vehicle_details(self):
        print("Vehicle Details")
        print()
        print(f"Vehicle Type :{self.details}")
    
    def fuel_type(self):
        print()
        print(f"Fuel Type : {self.fuel}")

    def rental_price(self):
        print(f"Rental Price : Rs.{self.charge}")

class Car(Vehicle):
    def __init__(self,charge,fuel,details):
        self.charge = charge
        self.fuel = fuel
        self.details = details

    def vehicle_details(self):
        print("Vehicle Details")
        print()
        print(f"Vehicle Type :{self.details}")
    
    def fuel_type(self):
        print()
        print(f"Fuel Type : {self.fuel}")

    def rental_price(self):
        print(f"Rental Price : Rs.{self.charge}")


class Bus(Vehicle):
    def __init__(self,charge,fuel,details):
        self.charge = charge
        self.fuel = fuel
        self.details = details

    def vehicle_details(self):
        print("Vehicle Details")
        print()
        print(f"Vehicle Type :{self.details}")
    
    def fuel_type(self):
        print()
        print(f"Fuel Type : {self.fuel}")

    def rental_price(self):
        print(f"Rental Price : Rs.{self.charge}")

VT1 = Bike(500,"Petrol","Bike")
VT1.vehicle_details()
VT1.fuel_type()
VT1.rental_price()

VT2 = Bike(3000,"Petrol","Car")
VT2.vehicle_details()
VT2.fuel_type()
VT2.rental_price()

VT3 = Bike(12000,"Diesel","Bus")
VT3.vehicle_details()
VT3.fuel_type()
VT3.rental_price()
'''

class Doctor(ABC):

    @abstractmethod
    def doctor_details(self):
        pass

    @abstractmethod
    def cosultation_fee(self):
        pass

    @abstractmethod
    def available_timings(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class Cardiologist(Doctor):
    def __init__(self,Department,Name,Fee,Timings,Treatment):
        self.Department = Department
        self.Name = Name
        self.Fee = Fee
        self.Timings = Timings
        self.Treatment = Treatment

    def doctor_details(self):
        print("Doctor Details")
        print(f"Department : {self.Department}")
        print(f"Doctor Name : {self.Name}")

    def cosultation_fee(self):
        print(f"Consultation Fee : Rs.{self.Fee}")

    def available_timings(self):
        print(f"Avaialable Timings : {self.Timings}")

    def treatment(self):
        print(f"Treatment : {self.Treatment}")


class Neurologist(Doctor):
    def __init__(self,Department,Name,Fee,Timings,Treatment):
        self.Department = Department
        self.Name = Name
        self.Fee = Fee
        self.Timings = Timings
        self.Treatment = Treatment

    def doctor_details(self):
        print("Doctor Details")
        print(f"Department : {self.Department}")
        print(f"Doctor Name : {self.Name}")

    def cosultation_fee(self):
        print(f"Consultation Fee : Rs.{self.Fee}")

    def available_timings(self):
        print(f"Avaialable Timings : {self.Timings}")

    def treatment(self):
        print(f"Treatment : {self.Treatment}")


class Orthopedic(Doctor):
    def __init__(self,Department,Name,Fee,Timings,Treatment):
        self.Department = Department
        self.Name = Name
        self.Fee = Fee
        self.Timings = Timings
        self.Treatment = Treatment

    def doctor_details(self):
        print("Doctor Details")
        print(f"Department : {self.Department}")
        print(f"Doctor Name : {self.Name}")

    def cosultation_fee(self):
        print(f"Consultation Fee : Rs.{self.Fee}")

    def available_timings(self):
        print(f"Avaialable Timings : {self.Timings}")

    def treatment(self):
        print(f"Treatment : {self.Treatment}")

DD1 = Cardiologist("Cardiology","Mr.Sharma",1500,"10:AM - 2:00 PM","Heart Diseases")
DD1.doctor_details()
DD1.cosultation_fee()
DD1.available_timings()
DD1.treatment()
print()

DD2 = Neurologist("Neurology","Dr.Rao",1800,"2:00 PM - 6:00 PM","Brain & Nervous System Disorder")
DD2.doctor_details()
DD2.cosultation_fee()
DD2.available_timings()
DD2.treatment()
print()



        

        


        



        
        

        
     

    
    





