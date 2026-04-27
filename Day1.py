Name = input("Enter your name")
Age = int(input("Enter your age"))
print("Hello"+ Name + ", you are a minor" if Age< 18 else "Hello" + Name +  ",You are an Adult")

#Don't use single line code . Not good for readability.

Num  = int(input("Enter Your Number"))
for i in range(1,Num+1):
    print(i)

#Remember if we use for loop , the loop will iterate , No need to use i+......

    

Num  = int(input("Enter Your Number"))
for i in range(1,Num+1):
    if i % 2 == 0:
        print("Even: " + i)
    else:
        print("Odd :"+i)

# use int(i) for concate


num = list(map(int,input("Enter your elements").split()))
for i in num:
    if i%2 == 0:
        print(f"Even :{i}")

#use split inside the num brackets


users = [ ]
for use in range(3):
     
     name = input("Enter name")
     age = int(input("Enter age"))

     user = {
          "name" : name,
          "age"  : age
            }
     
     users.append(user)
for use in users:
     if use["age"]>18:   #we need to check age of use  i.e single element ,not entire loop or dict.
           print(f"{use['name']}-{use['age']}")

        

users = []
def fun():
    name = input("Enter your name")
    age = int(input("Enter your age"))
    user = {
        "name" : name,
        "age"  : age
    }
    users.append(user)

while True:
    n = input("Enter yes if there is new record or Enter no")

    if n == "yes":
        fun()
    elif n == "no":
        break
    else:
        print("Enter valid input")
print(users)


 

d = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

for value in d.values():
    print(value)
for key,value in d.items():
    print(f"{key}:{value}")
    


    
