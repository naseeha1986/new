# Print all prime numbers between 1 and 50
n=int(input("Enter :"))
for i in range (2,n+1):
    prime = True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            prime =False
            break
    if prime:
            print(i)


            """  if i%2!=0:
         if i%3!=0:
             if i%5!=0:
                 if i%7!=0:
                     if i%11!=0:
                         print(i)"""
