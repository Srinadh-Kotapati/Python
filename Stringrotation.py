'''Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.

Input: s1 = "aab", s2 = "aba"
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.

Input: s1 = "abcd", s2 = "acbd"
Output: false
Explanation: Strings are not rotations of each other.'''

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
k = int(input("Enter number of rotations: "))
if str1[k+1] + str1[ :k] == str2:
    print(True)
else:
    print(False)