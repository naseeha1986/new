num=[3,7,2,9,4,1,6,8,5]
print("LENGTH OF THE LIST IS: ",len(num))

value=0
i=0
while i<len(num):
    value=value+num[i]
    i+=1
print("Sum of all elements in the list=", value)

num.sort()
print("The largest number in the list=",num[0])
print("The smallest number in the list=",num[8])

