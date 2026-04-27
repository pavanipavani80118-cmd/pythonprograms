n=int(input("Enter the value of n:"))
mylist=[]
for i in range(n):
    num=int(input("Enter a number:"))
    mylist.append(num)
    print("Even numbers are")
    print("[",end="")
    for num in mylist:
     if num%2==0:
      print(num,end=",")
      print("]")
      
