def Fibonacci(n):
    if n<0:
        print("Incorrect Input")
    elif n==0:
            return 0
    else:
         return Fibonacci(n-1)+ Fibonacci(n-2)
    n=int(input("enter the no"))
print(Fibonacci(9))
