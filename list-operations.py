# How do you insert an element at a specific position in a list

lis=[4,7,2,1,8,0,1,5,3,9,2]
n=input("Enter the position :")
ele=input("Enter the element to be inserted: ")
lis.insert(int(n),int(ele))
print(lis)

#How do you find the maximum and minimum values in a list?
mini=maxi=lis[0]
for i in range(len(lis)):
    if(mini>lis[i]):
        mini=lis[i]
    elif(maxi<lis[i]):
        maxi=lis[i]
    else:
        continue
print(f"Max:{maxi}  Min: {mini} ")
    

#How do you reverse a list?
stlis=["a","b","o","h"]
rev=stlis[::-1]
print(rev)

