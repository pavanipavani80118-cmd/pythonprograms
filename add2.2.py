import re
text="my phonr number is 9876543219"
print(re.findall (r"\d",text))
print(re.findall(r'\d{10}',text))
print(re.match(r'my',text))
print(re.search(r'phone',text))
