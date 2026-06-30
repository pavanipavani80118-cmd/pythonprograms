Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======================== RESTART: D:/25FFMCA026/12.1.py ========================
Meow
woof
>>> 
======================== RESTART: D:/25FFMCA026/12.2.py ========================
Traceback (most recent call last):
  File "D:/25FFMCA026/12.2.py", line 19, in <module>
    circle=circle("Red",5)
NameError: name 'circle' is not defined
>>> 
======================== RESTART: D:/25FFMCA026/12.2.py ========================
Circle area: 78.5
Rectangle area: <bound method Rectangle.area of <__main__.Rectangle object at 0x000001985EB40220>>
>>> 
======================== RESTART: D:/25FFMCA026/12.2.py ========================
Circle area: 78.5
Rectangle area: 24
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 12, in <module>
    obj=myclass()
NameError: name 'myclass' is not defined
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 14, in <module>
    obj.public_method()
AttributeError: 'myclass' object has no attribute 'public_method'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 14, in <module>
    obj.public_method()
AttributeError: 'myclass' object has no attribute 'public_method'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 14, in <module>
    obj.public_method()
AttributeError: 'Myclass' object has no attribute 'public_method'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 15, in <module>
    print(obj._protected_attribute)
AttributeError: 'Myclass' object has no attribute '_protected_attribute'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
i'm a protected attribute
i'm a protected method
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 17, in <module>
    print(obj.__Myclass__private__attribute)
AttributeError: 'Myclass' object has no attribute '__Myclass__private__attribute'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
i'm a protected attribute
i'm a protected method
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 17, in <module>
    print(obj._Myclass__private_attribute)
AttributeError: 'Myclass' object has no attribute '_Myclass__private_attribute'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
i'm a protected attribute
i'm a protected method
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 17, in <module>
    print(obj._myclass__private_attribute)
AttributeError: 'Myclass' object has no attribute '_myclass__private_attribute'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
i'm a protected attribute
i'm a protected method
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 17, in <module>
    print(obj._myclass__private_attribute)
AttributeError: 'myclass' object has no attribute '_myclass__private_attribute'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
i'm a protected attribute
i'm a protected method
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 17, in <module>
    print(obj.__myclass__private__attribute)
AttributeError: 'myclass' object has no attribute '__myclass__private__attribute'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
i'm a protected attribute
i'm a protected method
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 17, in <module>
    print(obj.__private_attribute)
AttributeError: 'myclass' object has no attribute '__private_attribute'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
i'm a protected attribute
i'm a protected method
i'm a private attribute
Traceback (most recent call last):
  File "D:/25FFMCA026/12.3.py", line 18, in <module>
    obj._myclass__private_method()
AttributeError: 'myclass' object has no attribute '_myclass__private_method'
>>> 
======================== RESTART: D:/25FFMCA026/12.3.py ========================
i'm a public attribute
i'm a public method
i'm a protected attribute
i'm a protected method
i'm a private attribute
i'm a private method
>>> 
======================== RESTART: D:/25FFMCA026/12.4.py ========================
Traceback (most recent call last):
  File "D:/25FFMCA026/12.4.py", line 22, in <module>
    print("Account Number:",account.get_amount_number())
AttributeError: 'BankAccount' object has no attribute 'get_amount_number'
>>> 
======================== RESTART: D:/25FFMCA026/12.4.py ========================
Account Number: 1234567890
Balance: 1000
Deposit Successful.
withdrawal successful.
Account Number: 9876543210
Balance: 5000
>>> 
======================= RESTART: D:/25FFMCA026/add1.1.py =======================
Array elements are:
10
20
30
40
50
>>> 
======================= RESTART: D:/25FFMCA026/add1.2.py =======================
Traceback (most recent call last):
  File "D:/25FFMCA026/add1.2.py", line 2, in <module>
    arr=arr('i',[10,20,30,40,50])
NameError: name 'arr' is not defined
>>> 
======================= RESTART: D:/25FFMCA026/add1.2.py =======================
Sum of array elements= 150
>>> 
======================= RESTART: D:/25FFMCA026/add1.3.py =======================
Enter element to search:
======================= RESTART: D:/25FFMCA026/add1.3.py =======================
Enter element to search:
======================= RESTART: D:/25FFMCA026/add1.3.py =======================
Enter element to search:
======================= RESTART: D:/25FFMCA026/add1.3.py =======================
Enter element to search: