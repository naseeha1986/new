num=list(map(int, input("Enter the number in list").split()))
even=0
odd=0
for n in num:
    if n%2==0:
        print(f"{n}is even")
        even +=1
    else:
        print(f"{n}is odd")
        odd+=1
print(f"\nTotal Even number: {even}")
print(f"Total odd number: {odd}")
        
