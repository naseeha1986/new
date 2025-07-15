#finding largest among number
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter Third number:"))
if n1>=n2:
    if n1>=n3:
        print(f"{n1} is Greater")
    else:
         print(f"{n3} is greater")
elif n2>=n3:
    print(f"{n2} is greater")
else:
    print(f"{n3} is greater")
