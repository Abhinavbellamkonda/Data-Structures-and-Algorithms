#Naive Approach
#Brut if n<=1 then it will be 1 or it will f(n-1) + f(n-2)
#Expanding the Calculations
'''fib(4) = fib(3) + fib(2)
       = (fib(2) + fib(1)) + (fib(1) + fib(0))
       = ((fib(1) + fib(0)) + fib(1)) + (fib(1) + fib(0))
       = ((1 + 0) + 1) + (1 + 0)
       = (1 + 1) + (1 + 0)
       = 2 + 1
       = 3 ✅'''

n = int(input("Enter n :"))
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(n))

#Efficient Algorithm
#Think of how we do it with hand we will simply calculate last 2 integers.
#Initialize a Array as we know the first 2 elements are 0,1 and size would be 0*(n-1) then we will calculate last 2 integers from array
#for loop starts from 2 ad ends at n+1
def fibonacciEf(n):
    array = [0,1] + [0] * (n-1)
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        for i in range(2,n+1):
            array[i] = array[i-1] + array[i-2]
        return array[n]
print(fibonacciEf(n))