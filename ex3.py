#Check whether a year is a leap year or not
year=int(input("Enter any year to check leap year or not:"))
if year%4==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
