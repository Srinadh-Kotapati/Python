
#Write a program to take a string from the user and:

   # a.Convert it to uppercase

    #b.Convert it to lowercase
string = input("Enter string:")
print(string.upper())
print(string.lower())


#Write a program to count the number of vowels in a given string using string methods.
s = input("Enter string:")
count = 0
for i in s:
    if i in "aeiouAEIOU":
        count += 1
print(count)



#Write a program to check whether a given string starts with a specific word using a string method.
s = input("Enter a sentence:")
n = s.split(" ")
check = "write"
if n[0].lower() == "write":
    print("matched")
else:
    print("Not matched")

    

#Write a program to replace all spaces in a string with a hyphen (-).
s = input("Enter a sentence:")
n = s.replace(" ","-")
print(n)


#Write a program to find the length of a string without using the len() function.
s = input("Enter a string:")
count = 0
for i in s:
    count = count+1
print(count)



#Write a program to check whether a given string is a palindrome using string methods.
s = input("Enter a value:")
if s == s[::-1]:
    print("Palindrone")
else:
    print("Not a palindrone")

    

#Write a program to count the number of words in a sentence.
s = input("Enter a sentence:")
n = s.split(" ")
print(len(n))



#Write a program to find how many times a particular character appears in a string.
s = input("Enter a sentence:")
c = "s"
count = 0
for i in s :
    if i == c:
        count = count+1
print(count)


#Write a program to remove leading and trailing spaces from a string.
s = input("Enter a sentence:")
n =s.replace(" ","")
print(n)



#Write a program to check whether a string contains only digits using string methods.
s = input("Enter a string:")
if s.isdigit():
        print("Yes,String contain only digits")
else:
        print("No, it has other than digits")




