str1="https://geeksforgeeks.org/data-structures"
str2="https://geeksforgeeks.org/"
if str2 in str1:
    str2=str1[len(str2):]
print str2
