x=input("Enter the string:")

#Reversing 
print("Reversed String: ")
print(x[::-1])

"""Enter the string:
hellooo i am annu
Reversed String: 
unna ma i ooolleh"""


#reverses the order of each word in the string
word=x.split()
words=word[::-1]
words=" ".join(words)
print("Reversed order: "+ words)
'''Enter the string:
hello i am annnu
Reversed order: annnu am i hello'''

#reverse each word in the string
out=x.split(" ")
o1=[]
for i in out:
    o1.append(i[::-1])
o1=" ".join(o1)
print( "Reversed each word without changing the order :"+ o1)
'''Enter the string:
hello i am annu

Reversed each word without changing the order :olleh i ma unna'''