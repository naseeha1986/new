age=int(input("Enter Your age:"))
income=int(input("Enter Your Annual Income:"))
if age>=21 and age<=60:
    if income>=30000:
        print("YOU ARE ELIGLIBLE FOR LOAN")
    else:
        print("YOUR INCOME IS LOW TO APPLY FOR LOAN")
else:
    print("YOU are not ELIGIBLE FOR LOAN")
