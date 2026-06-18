#Create a lambda function to find the square of a number
square = lambda x:x*x
print(square(5))

#Create a lambda function to calculate the total price (price × quantity).
total_price = lambda price,quantity:price*quantity
print(total_price(100,3))

#Create a lambda function that checks whether a number is even or odd.
check = lambda x:'even' if x%2==0 else 'odd'
print(check(8))


#Create a function apply_operation(func, a, b)......It should take a function and two numbers.
def apply_operation(func,a,b):
    return func(a,b)
s = lambda a,b:a+b
multiple= lambda a,b:a*b
print(apply_operation(s,3,5))
print(apply_operation(multiple,6,5))


#Create a function multiplier(n) that returns a function to multiply any number by n.
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)

print(double(5))


#Given a list of numbers, use map() to return a list of squares.
a = [2,3,4,5,6,7,8]
l = list(map(lambda x:x*x,a))
print(l)

def square():
    l = list(map(int,input("Enter numbers:").split()[:6]))
    a = [i*i for i in l]
    print(a)
square()


#Convert a list of names to uppercase using map().
a = ['srinadh','vamsi','vara','krishna']
l = list(map(lambda x:x.upper(),a))
print(l)


#Use filter() to extract even numbers from a list.
a = [2,1,3,4,5,6,7,8,9]
f = list(filter(lambda n:n%2 == 0,a))
print(f)


#Given a list of marks, filter students who scored 50 or above
marks = [43,55,45,67,75,87,76]
f = list(filter(lambda x:x>50,marks))
print(f)


#Use reduce() to find sum of elements.
from functools import reduce
a = [9876,74665,4647,36464]
r = reduce(lambda x,y:x+y,a)
print(r)

#Use reduce() to find product of elements.
from functools import reduce
a = [23,45,67,43,22]
r = reduce (lambda x,y:x*y,a)
print(r)


#Given a list of prices, apply 10% discount to each price.
l = [100,200,200]
r = list(map(lambda x:x-(x*0.10),l))
print(r)


#Given a list of salaries, filter salaries above 50,000.
l = [30000,35000,55000,45000,50500,60000,70000]
f = list(filter(lambda x:x>50000,l))
print(f)


#Given a list of item prices in cart, calculate total bill.
from functools import reduce
l = [250,150,100]
r = reduce(lambda x,y:x+y,l)
print(r)

#Given a list of numbers:
#* First filter even numbers.......* Then square them using map()
l = [1,2,3,4,5,6,7,8,9]
even_numbers = list(filter(lambda x:x%2==0,l))
print(even_numbers)
m = list(map(lambda x:x**2,even_numbers))
print(m)
