'''Print a Pyramid Pattern

    *    
   ***   
  *****  
 ******* 
*********
'''
n=5
temp=n
for i in range(1,2*n+1,2):
    for j in range(temp,0,-1):
        print(" ",end="")
    temp-=1   
    print("*"*i)

