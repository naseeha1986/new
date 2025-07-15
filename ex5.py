# Generate multiplication table of a number (1 to 10)
num= int(input("Enter which table YOU need to get output:"))
for i in range(1,11,1):
               print (f"{num} x {i} = {num*i}")






               
#using while loop
no=int(input("Enter which table YOU need to get output:"))
i=1
while i<=10:
    print (f"{no} x {i} = {no*i}")
    i+=1
