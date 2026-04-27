Mylist=input("Enter a list of numbers are seperates by space:")
mylist=list(map(int,Mylist,Split()))
sum=0
for num in mylist:
 sum+=num
 print("The sum of the numbers is:",sum)
