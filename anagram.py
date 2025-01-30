
# How do you check if two strings are anagrams of each other?
str=input("Enter the string: ")
str2=input("Enter the other string: ")
flag=1
for i in str:
    if(str.count(i)==str2.count(i)):
        flag=1
    else:
        print("Not anagram")
        flag=0
        break
if(flag==1):
    print("Anagram")
        
