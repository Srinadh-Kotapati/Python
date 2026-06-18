#Write a program that takes a list of numbers and uses built-in functions to print:

#* Maximum value
#* Minimum value
#* Sum of elements
#* Length of the list

l = list(map(int,input("Enter elements").split()[:6]))
print(l)
print(max(l))
print(min(l))
print(sum(l))
print(len(l))


# User-Defined Max, Min, Sum (Without Built-ins)
#Write your own functions to calculate: * Maximum ,* Minimum,* Sum
def maximum():
    l = list(map(int,input("Enter elements:").split()[:6]))
    sum = 0
    for i in range(0,len(l)):
        for j in range(0,len(l)-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    print(l)
    print(l[-1])
    print(l[0])
maximum()


def sum_of_list():
     l = list(map(int,input("Enter elements:").split()[:6]))
     sum = 0
     for i in l:
          sum += i
     print(sum)
sum_of_list()



#Create a function greet(name) that prints a greeting message   
def greet(name):
    return f"Hello {name}! Welcome to Python class."
print(greet("srinadh"))


#Create a function that returns total amount.
def calculate_total(price, quantity):
    return price*quantity
print(calculate_total(100,3))


#Create a function with default role.
def create_account(name, role = 'admin'):
    return f"Account created for {name} with role {role}"
print(create_account("srinadh","developer"))


#* One function that prints square .......* One function that returns square
def square(x):
    return x*x
print(square(5))

def square2(y):
    return y*y
s = square2(6)
print(s*10)


#Create two functions: add(a, b) and multiply(a, b).....Call multiply using result of add.
def add(x,y):


#Write a function that returns count of even and odd numbers.

def even_odd_count(n):
    l = list(map(int,input("Enter elements:").split()[:n]))
    even_count =0
    odd_count=0
    for i in l:
        if i%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(even_count)
    print(odd_count)
even_odd_count(6)


#Palindrome Checker
def palindrone(n):
    if n ==n[::-1]:
        return True
    else:
        return False
print(palindrone("madam"))


#Write a recursive function to find factorial.
def factorial(n):
    if n == 0 or n ==1:
        return 1 
    else:
        return n*factorial(n-1)
print(factorial(5))





    

    







    