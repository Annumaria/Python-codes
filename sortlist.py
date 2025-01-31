
#How do you sort a list in ascending and descending order?
l=[4,2,6,2,7,1,8,0]
n=len(l)
#ascending order- bubble sort
for i in range(n):
    for j in range(n-1):
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)   

#descending order in selection sort


#How do you rotate a list to the right by k places?