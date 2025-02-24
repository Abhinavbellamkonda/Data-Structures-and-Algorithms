1.Fibonacci Sequence
What is Fibonacci?
The Fibonacci sequence is a series of numbers where each number is the sum of the two previous numbers.

Fibonacci Series
Copy
Edit
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …
Starts with 0 and 1.
Each next number is the sum of the two before it.

Fibonacci Formula
F(n)=F(n−1)+F(n−2)
F(0) = 0
F(1) = 1
F(2) = 1 (0 + 1)
F(3) = 2 (1 + 1)
F(4) = 3 (1 + 2)
F(5) = 5 (2 + 3)

Fibonacci Using Recursion (Slow Method)
python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55
Problem: Very slow for large numbers because it repeats calculations.

Fastest Fibonacci Using Iteration
python
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fibonacci_iterative(10))  # Output: 55
Time Complexity: O(n)
Space Complexity: O(1) (No extra memory needed!)

2.Greatest Common Divisor (GCD)
What is GCD?
The Greatest Common Divisor (GCD) of two numbers is the largest number that divides both numbers exactly.

Examples
mathematica
Copy
Edit
GCD(12, 18) = 6  (because 6 is the biggest number that divides both 12 and 18)
GCD(48, 18) = 6
GCD(56, 98) = 14
GCD(101, 103) = 1  (because 101 and 103 are prime numbers)

Naïve GCD Method (Slow)
Step-by-step Explanation
Find the smaller number of a and b.
Check every number from 1 to min(a, b).
Find the largest number that divides both.
Example: GCD(48, 18)
yaml
Copy
Edit
Divisors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48
Divisors of 18: 1, 2, 3, 6, 9, 18
Common Divisors: 1, 2, 3, 6
Largest common divisor = 6

Python Code
def naive_gcd(a, b):
    gcd_value = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i  # Update the largest divisor
    return gcd_value

print(naive_gcd(48, 18))  # Output: 6
Problem: Slow for large numbers because it checks every number up to min(a, b).

 Efficient GCD: Euclidean Algorithm (Fast)
Instead of checking all numbers, the Euclidean Algorithm reduces the problem step by step.

gcd(a,b)=gcd(b,a mod b)
Keep replacing a with b and b with a % b until b = 0.
The last a value is the GCD.

Step-by-Step Example: GCD(48, 18)
gcd(48, 18)
       = gcd(18, 48 % 18)
       = gcd(18, 12)   (48 % 18 = 12)

       = gcd(12, 18 % 12)
       = gcd(12, 6)    (18 % 12 = 6)

       = gcd(6, 12 % 6)
       = gcd(6, 0)     (12 % 6 = 0)

       GCD = 6
Python Code

def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd_Euclidean(48, 18))  # Output: 6
Time Complexity: O(log(min(a, b)))
Much faster than the naïve method

Summary Table
Topic	Definition	Best Method	Time Complexity
Fibonacci	Series where each number is the sum of the previous two	Iterative Fibonacci	O(n)
GCD	Largest number that divides both a and b	Euclidean Algorithm	O(log(min(a, b)))