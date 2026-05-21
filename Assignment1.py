
#Program to Calculate the Area of a Circle
#Problem Statement: Write a program to calculate the area of a circle. The program should take the radius as input and calculate the area of the circle. Use the appropriate constant for (\pi) to perform the calculation.
R = int(input("enter radis of circle:"))
A = 3.1416  * (R)**2
print(A)

#Program to Calculate Total Cost After Discount
#Problem Statement: Write a program to calculate the total cost after applying a discount. The program should take the original price and discount percentage as input, and then calculate the price after applying the discount.
Original_price = int(input("Enter original price:"))
Discount = int(input("Enter discount:"))
final_price = Original_price *(1-Discount/100)
print(final_price)


#Program to Calculate Simple Interest
#Problem Statement: Write a program to calculate the simple interest. The program should take the principal amount, rate of interest, and time in years as input, and calculate the simple interest.
P = int(input("Enter total principal amount:"))
T = int(input("Enter Time:"))
R = int(input("Enter rate of interest:"))
simple_interest = (P*T*R)/100
print(simple_interest)


#Program to Calculate Total Salary
#Problem Statement: Write a program to calculate the total salary of an employee. The program should take the basic salary, House Rent Allowance (HRA), and Dearness Allowance (DA) as input and calculate the total salary.
Basic_salary = int(input("Enter basic salary:"))
Hra = int(input("Enter hra:"))
Da = int(input("Enter Da:"))
Total_salary = Basic_salary + Hra + Da
print(Total_salary)


#Program to Calculate Distance Traveled
#Problem Statement: Write a program to calculate the distance traveled by a vehicle. The program should take the speed of the vehicle and the time it has been traveling as input, and calculate the total distance traveled.
Speed = int(input("Enter speed :"))
Time = int(input("Enter Time:"))
Distance = Speed * Time
print(Distance)


#Program to Convert Temperature from Celsius to Fahrenheit
#Problem Statement: Write a program to convert a temperature from Celsius to Fahrenheit. The program should take the temperature in Celsius as input and convert it into Fahrenheit.
Celsius = int(input("Enter Temperature in Celsius:"))
F = ((9/5)*Celsius)+32
print(F)

#Program to Find the Maximum of Two Numbers Using Ternary Operator
#Problem Statement: Write a program to find the maximum of two numbers using the ternary operator. The program should take two numbers as input and output the larger of the two.
N1 = int(input("Enter first number:"))
N2 = int(input("Enter second number:"))
Max = N1 if N1 > N2 else N2
print(Max)


#Swap Two Numbers
#Problem Statement: Write a program to swap two numbers without using a third variable. The program should take two numbers as input and swap their values.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
a,b = b,a
print(a,b)


#Next Multiple of 100
#Problem Statement: Write a program to find the next multiple of 100 greater than a given number. The program should take a number as input and output the next multiple of 100.
n = int(input("Enter a number:"))
if n % 100 == 0:
    print(n)
else:
    n = ((n // 100) + 1) * 100
    print(n)


#Splitting into the Teams
#Problem Statement: Write a program to divide a group of people into teams of two. The program should take the number of people as input and output the number of teams that can be formed and how many people will be left without a team.
n = int(input("Enter number of players:"))
teams = n // 2
reamin = n%2
print(teams)
print(reamin)