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

    
