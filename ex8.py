text=input("Enter a string or number:")
if str(text)==str(text)[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not palindrome")
