n=int(input("enter limit of fibonacci series :"))
for i in range(0,n,1):
    if i==0:
        n1=i
        print(i)
    if i==1:
        n2=i
        print(i)
    if i>1:
       n3=n1+n2
       print(n3)
       n1=n2
       n2=n3
       
