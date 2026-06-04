def fibonacci(Number):
    if(Number==0):
        return 0
    elif Number==1:
        return 1
    else:
        return fibonacci(Number-2)+fibonacci(Number-1)
Number=int(input("please enter the fibonacci number range="))
sum=0
for Num in range(Number):
    print(fibonacci(Num),end='')
sum=sum+fibonacci(Num)
print("\n the sum of fibonacci series numbers=%d"%sum)
