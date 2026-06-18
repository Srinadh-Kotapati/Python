'''
n = int(input("Enter number of elements:"))
l =[]
for i in range(n):
    a = input()
    l.append(a)
print(l)


a = list(map(int,input().split()[:3]))


#reversing a list
a = [1,2,3,4,5,6]
mid = len(a)//2
print(mid)
inc = a[:mid]
dec = a[mid:]
inc.reverse()
dec.reverse()
r = inc+dec
print(r)

#sum = target
l = [0,2,3,4,5,6,7,8]
target = 8
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if l[i]+l[j] == target:
            print((i,j))

            

#sorting values
l = [1,2,0,1,0,2,1,0]
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)


#reversing an array
a = [1,2,3,4,5,6]
a.reverse()
print(a)

#printing union values using loops
a = [2,4,5,6,7]
b = [4,5]
c = []
d = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
for i in a:
    for j in b:
        if i != j:
            d.append(i)
            

print(f"union {c}")
print(f"intersection {set(d)}")


# [1, 2, 3, 4, 5].....Output: [5, 1, 2, 3, 4]
l = [1,2,3,4,5,6]
for i in range(0,len(l)-1):
    l[i] = l[i+1]
print(l)
'''

# Function to check whether any pair exists
# whose sum is equal to the given target value
class Two_sum:
    def two_sum(self,arr, target):
     sum = 0
    # Sort the array
    

     left, right = 0, len(arr) - 1

    # Iterate while left pointer is less than right
     while left < right:

        sum = arr[left] + arr[right]


        # Check if the sum matches the target
        if sum == target:
           return arr[left],arr[right]
            
        elif sum < target: 
            left += 1  # Move left pointer to the right
        else:
            right -= 1 # Move right pointer to the left

    # If no pair is found
     return False

arr = list(map(int,input("Enter numbers").split()))
target = 7

obj = Two_sum()
result =obj.two_sum(arr,target)
if result:
   print(result)
else:
   print("No pair")







