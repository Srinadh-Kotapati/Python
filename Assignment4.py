#Assignment4- srinadh
#1.Write a program to check whether a given number is positive, negative, or zero.

n = int(input("Enter a number:"))
if n == 0:
    print("Input number is zero")
elif n < 0:
    print("Input number is negative")
else:
    print("Input number is positive")

    

#2.Write a program to check whether a given number is even or odd using an if-else statement.

n = int(input("Enter a number:"))
if n % 2 == 0:
    print("n is a even number")
else:
    print("n is odd number")
    
    

#3.Write a program to find the largest of two numbers entered by the user.
n1 = int(input("Enter your first number:"))
n2 = int(input("Enter your second number:"))
print(max(n1,n2))
if n1 < n2:
    print("n2 is larger than n1")
else:
    print("n1 is larger")

    

#4.Write a program to find the largest of three numbers using if-elif-else.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a > b and a > c:
    print("a is greater than b and c")
elif b > a and b > c :
    print("b is greater than a and c")
else:
    print("c is greater than a and b")

    

#5.Write a program to check whether a given year is a leap year or not.
Year = int(input("Enter a year:"))
if Year % 4 == 0 and Year % 100 != 0:
    print("It's leap year")
elif Year % 400 == 0:
    print("It's leap year")
else:
    print("It's not leap year")
    


#6.Write a program to check whether a person is eligible to vote based on age input.
Age = int(input("Enter your age:"))
if Age < 0:
    print("Age is invalid!")
elif Age >= 0 and Age < 18:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")

    

#7.Write a program to display student grade based on the following conditions:

   # Marks ≥ 90 → Grade A
   # Marks ≥ 75 → Grade B
   # Marks ≥ 60 → Grade C
   # Marks < 60 → Grade D

marks = int(input("Enter your marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks < 60 :
    print("Grade D")
elif marks < 0 or marks > 100:         #Doubt 
    print("Invalid marks")

    

#8.Write a program to check whether a given character is: a vowel or a consonant
a = "AEIOUaeiou"
n = input("Enter a character:")
if n in a:
    print("It is a vowel")
else:
    print("It is a consonant")



#9.Write a program to create a simple calculator using if- elif -else
#(addition, subtraction, multiplication, division).
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
op = input("Enter any operator in(+,-,*,/,//,**,%)")
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op =="/":
    print(a/b)
elif op == "//":
    print(a//b)
elif op == "**":
    print(a**b)
elif op == "%":
    print(a%b)
else:
    print("Invalid operator")



#10.Write a program to check whether a given number is a three-digit number or not using conditional statements.
a = int(input("Enter a number: "))
if len(str(a))== 3:
    print("It is a threee digit number")
else:
    print("It is not a three digit number")

