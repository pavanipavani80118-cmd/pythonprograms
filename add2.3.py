import re
text="Devops123"
if re.match(r'^[A-Z,a-z,0-9]+$',text):
    print("Alphanumeric String")
else:
    print("Not Alphanumeric")
