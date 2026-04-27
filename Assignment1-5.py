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
