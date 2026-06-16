try:
   num=int(input("Enter a number:"))
   result=10/num
except ValueError:
    print("Error:Invalid input!please enter a valid number.")
except ZeroDivisionError:
    print("Error:Division by zero!")
else:
    print("Result:",result)
