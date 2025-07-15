#Calculate the factorial of a number
n= int(input("Enter any number to get its factorial:"))
if n==1 or n==0:
    print (1)
else:
    for i in range (2,n,1):
        n*=i    
print(n)           
