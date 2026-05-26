#Largest number using loops

arr = list(map(int,input().split()))
print(arr)
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        arr[i+1],arr[i] = arr[i],arr[i+1]
print(arr[-1])


a = "hadskjksuhftgfr hjfvdsfdskwopfvk" 
for i in a:
    if a.count(i) == 1:
        print(i)
        break
        
name = "Vijay Thalapathy"
count = 0
for i in name:
    if i in "AEIOUaeiou":              #Counting vowels
        count += 1
print(count)



name = "srinadh"
s = name[::-1]
print(s)

s = "121"
if s == s[::-1]:
    print("Palindrone")
else:
    print("Not a Palindrone")

    
name = "Vijay Thalapathy".lower()
for i in name:
    if i in "aeiou":
        s =name.replace(i,"*")
print(s)


name = "Vijay Thalapathy"
f = {}
for i in name:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
print(f)


name = "Vijay Thalapathy"
count = 0
for i in name:
    count += 1
print(count)


name = "Vijay Thalapathy"
for i in name:
    if name.count(i) > 1:
        a = name.replace(i,"")
print(a)


arr = [12, 32,1, 4, 76,2]
l = arr[0]
sl = arr[0]
for i in arr:
    if i > l:
        l = i

for i in arr:  
    if i > sl and i != l:
        sl = i
print(sl)

#sorting a list manually
a = [9,8,7,6,5,4,3,2]
for j in range(len(a)-1):
    for i in range(len(a)-1):
      
      if a[i] > a[i+1]:

        a[i],a[i+1] = a[i+1],a[i]
print(a)


#Remove duplicates from list.

a = [8,7,4,5,2,7,3,5,6,8,4,3]
s = []
for i in a:
    if i not in s:
        s.append(i)
print(s)

        
#Find sum of list elements.
a = [8,7,4,5,2,7,3,5,6,8,4,3]
s = 0
for i in a:
    s =  s+i
print(i)    


a = [1,3,0,4,7,0,5,0,3,1]
for i in range(0,len(a)):
    for j in range (0,len(a)-1):                  
        if a[j] == 0:
            a[j],a[j+1] = a[j+1],a[j]
print(a)







