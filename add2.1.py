import re
email=input("enter email:")
pattern=r'^[a-z,A-Z,0-9._%+-]+@[a-z,A-z,0-9-]+\.[a-z,A-z]{2,}$'
if re.match(pattern,email):
    print("Valid Email Adress")
else:
    print("Invalid Email Address")
