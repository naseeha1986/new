print("GETTING INPUT FROM USER")
num=list(map(int, input("Enter numbers seperated by space:").split()))
print("ENTERED LIST IS:\n",num)

l=len(num)-1
num.sort()
print("FINDING MAXIMUM AND MINIMUM NUMBERS")
print("maximum value in this list:",num[int(l)])
print("minimum value in this list:",num[0])

print("SUM OF ALL ELEMENTS IN THE LIST:")
value=0
i=0
while i<len(num):
    value=value+num[i]
    i+=1
print("SUM=", value)

i=0
while i<len(num):
    if num[i]%2==0:
        num.pop(i)
    i+=1
print("list after removal of even number",num)
