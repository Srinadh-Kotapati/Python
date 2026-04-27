a = ("a", "b","c",1,2,3,4,"%")       #Defining list                         
print(a[0])                          # First element
print(a[2])                          # Third element
print(a[-1])                         # last element
print(a[4])                          # fifth element

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
