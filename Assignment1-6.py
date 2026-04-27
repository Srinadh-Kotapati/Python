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
