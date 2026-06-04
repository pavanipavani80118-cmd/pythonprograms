def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
x=input("Enter the first integer:")
y=input("Enter the second integer:")
if x.isdigit()and y.isdigit():
    a=int(x)
    b=int(y)
    result=gcd(a,b)
    print(f"The gcd of{a}and{b}:",result)
else:
    print("please enter valid integers:")
