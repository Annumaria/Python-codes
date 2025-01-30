#How do you check if a string contains a specific substring?
str=input("Enter the string: ")
sub=input("Enter the substring: ")
if(str.find(sub)>0):
    print("Substring present")
else:
    print("Substring not present")
    
'''Enter the string: 
annu
Enter the substring: 
opp
Substring not present'''


#How do you find the frequency of a character in a string?
a=str.count(sub)
print(f"No of occurences: {a}")
#How do you remove all vowels from a given string?
vowels=["a","e","i","o","u"]
out=""
for i in str.lower():
    if(i in vowels):
        out=str.replace(i,"")
print(f"No vowels:{out} ")
