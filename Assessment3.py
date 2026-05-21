#Assignment3-srinadh.k
#Write a program to demonstrate all arithmetic operators using two user-defined numbers.

input_1 = int(input("Enter first number:"))     
input_2 = int(input("Enter second number:"))    

           
print(input_1 + input_2)       
print(input_2-input_1)         
print(input_1*input_2)         
print(input_1/input_2)         
print(input_1**input_2)        
print(input_1//input_2)        
print(input_1%input_2)         


#Write a program to compare two numbers using relational operators and display the result.

inp1 = int(input("Enter first number:"))     
inp2 = int(input("Enter second number:"))    
print(inp1 == inp2)                          
print(inp1 > inp2)                           
print(inp1 < inp2)                          
print(inp1 >= inp2)                          
print(inp1 <= inp2)                          
print(inp1 != inp2)                          


#Explain logical operators (and, or, not) with a truth table and a sample program.

# A      B      A and B
#T       T         T
#T       F         F
#F       T         F
#F       F         F
#True only when both conditions are True

a = 6
b = 8
c = 12
print(a < b and b < c)          #True 
print(a > b and b < c)          #False

# A       B       A or B
#T        T         T
#T        F         T
#F        T         T
#F        F         F
# True when one of the condition is True

print(a > b or b < c)       #True 
print(a < b or b < c)       #True
print(a > b and b > c)      #False

# A      not A
#T         F
#F         T

print(not(a > b))            #True
print(not(a < b))            #False


#Write a program to check whether a number lies between 10 and 50 using logical operators.
n = int(input("Enter your number:"))
if n > 10 and n < 50:
    print(" Number lies between 10 and 50")
else:
    print("Number doesn't lies between 10 and 50")

print(n > 10 and n <50)

#Demonstrate the use of assignment operators (=, +=, -=, *=, /=) with examples.
a = 5
print(a)      
a += 1
print(a)      
a -=1 
print(a)      
a *= 2
print(a)      
a /= 2
print(a)      



#Write a program to check whether a given value exists in a list using membership operators.
a = [1,2,3,4,6,7,8]
print(1 in a)        #True
print(5 in a)        #False
print(6 not in a )   #False



#What is the difference between == and is operators? Write a program to prove it.
a = [1,2,3]
b = [1,2,3]
print(a == b)          #True. Because a and b both have values.
print(a is b)          #False.is compares whether two variables refer to the same object in memory.


#Write a program to check whether a number is even or odd using operators.
n = int(input("Enter a number:"))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")

    

#Write a program to calculate the area of a rectangle using arithmetic operators and user input.
l = int(input("Enter length of rectangle:"))
b = int(input("Enter breadth of rectangle:"))
area = l * b
print(area)


#Explain operator precedence in Python and write a program showing how precedence affects the result.

print(5+5-3*2/3*5%3//2)  #10.0

#Order of precedence (), **, +i, -i, *, /, //, %, +, -, <, >, ==,!=, <=, >=, not, and, or.


