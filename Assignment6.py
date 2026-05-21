#Write a program to print numbers from 1 to N using a loop.
#(N is given by the user)
'''

n = int(input("Enter the number:"))
for i in range(0,n+1):
    print(i)
    i += 1


#Write a program to find the sum of all even numbers between 1 and N using a loop.
n = int(input("Enter a number:"))
s = 0
for i in range(0,n+1):
    if i % 2 == 0:
        s += i
print(s)



#Write a program to reverse a given number using a loop.
#Example: Input → 1234, Output → 4321
n = input("Enter a number:")
s = int(n[::-1])
print(s)



#Write a program to count the number of digits in a given number using a loop.
n = input("Enter a number:")
c = 0
for i in n:
    if i.isnumeric():
        c += 1
print(c)



#Write a program to generate the multiplication table of a given number up to 10.
#expected
 
'''
#output : 
#5 * 1 = 5
#5 * 2 = 10
#5 * 3 = 15
#5 * 4 = 20


'''
n = int(input("Enter a number:"))
for i in range(1,11):
    print(n ,"X",i,"=",n*i)
        
    

#.Write a program to print a square pattern of stars of size N:

#****
#****       
#****
#****
n = int(input("Enter a number:"))
for i in range(1,n+1):
    print(n*"*")

for i in range(1,n+1):
    print(n*" *")

    '''

#Write a python program to print a complete diamond shape using stars (*) with nested loops.
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    '''
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end ="")
    for j in range(2*i-1):
        print("*",end="")
    print()
'''
num = 1
for i in range(4):
    for j in range(5):
        print(num, end=" ")
        num += 1
    print()
        
        '''
