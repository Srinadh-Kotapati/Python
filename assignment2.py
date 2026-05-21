#Srinadh_Kotapati

students = ["first","second","Third","Fourth","Fifth"]
print(students)                  
students.append("sixth")          
students.remove(students[1])     
students.pop(2)         
print(students)




a = list(map(int, input("Enter Numbers: ").split()))
print(a)
a.sort()
print(a)
print("Maximum :" + str(a[-1]))
print("Minimum :"+str(a[0]))



a = ("a", "b","c",1,2,3,4,"%")                             
print(a[0])                          
print(a[2])                         
print(a[-1])                         
print(a[4])                      

#A tuple is called as immutable, which means once it is created, its elements cannot be changed, added, or removed.
a[0] = "x"                          # shows up an error "TypeError: 'tuple' object does not support item assignment"

#Converting tuple into list
temp = list(a)
print(temp)
temp[0] = "z"                        # Adding element
print(temp)
  
#Converting a list into tuple
a = tuple(temp)
print(a)


#Program Four

#Defining a list
a = [1,2,2,3,3,4,4,5,5]
print(set(a))


#Program Five
# Creating dictionary with employee details

employees = {
    1: {"name": "a", "salary": "2k"},
    2: {"name": "b", "salary": "3k"},
    3: {"name": "c", "salary": "4k"}
}

print(employees)

#Adding key
employees[1]["age"] = "22"
print(employees[1])

#updating salary
employees[2]["salary"] = "6k"
print(employees[2])

#Deleting salary
del employees[3]["salary"]
print(employees[3])



#Program six
# Dictionary
student = {
    "id": 1,
    "name": "Srinadh",
    "course": "Python full stack",
    "marks": 100
}

# Printing all Keys
print("Keys:")
for key in student.keys():
    print(key)

# Printing all Values
print("Values:")
for value in student.values():
    print(value)

# Printing all  Key-Value Pairs
print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

    

#Program seven
# Defining two sets
a = {1, 2, 3, 4, 5, 6, 7}
b = {6, 7, 8, 9, 10}

# Printing sets
print("Set A:", a)
print("Set B:", b)

# printing a Union b
print( a | b)

#Printing a Intersection b
print( a & b)

# Printing a Difference b
print( a - b)
# Printing b Difference a
print( b - a)


#program eight
# Defining a List
a = ['a', 'b', 'c', 'd', 'c', 'a', 'b', 'e', 'f']

# Empty dictionary to store count of frequency
freq = {}

# Counting frequency
for item in a:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Printing frequency of elements

for key, value in freq.items():
    print(key, ":", value)

    

#Program nine
#List
a = ["a","b","c","d","e"]
#used to store values . A list stores multiple items in order and can be changed.
#Ex : Shopping cart items in stores

#tuple
location = (17.3850, 78.4867,13.54674,16.64748)
#A tuple is like a list but cannot be changed after creation.
#used for GPS coordinates (latitude, longitude).

#set
c = {1,3,4,5,6,7}
#Used to store unique values

#Dict
student = {
    "id": 1,
    "name": "srinadh",
    "marks": 100,
    "subject":"Python"
}
#Used to store values in key-value pair
#Database