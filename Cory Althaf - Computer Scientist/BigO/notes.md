## What is Algorithm

The Algorithm is a definite, effective, and finite process that receives input and produces output based on the input - Donald Knuth's

- Definiteness means steps are clear, correct and unambiguous.
- effectiveness means you can perform each operation precisely to solve the problem.
- Finiteness means that the Algorithm stops after a finite number of steps.

*tip - Think of a runner in a race track. He need to run in track, should watch out his each step to win in race and always runner should stop at destination*

How do you know which algorithm is best? Is it simple? The fastest? The Smallest? Or Something else?

We will judge the Algorithm by run time.

Lets take a example of sorting a list, we can sort list in many ways.

for example:

```
import time

start = time.time()
for i in range(5):
 print("Hello World")
end = time.time()
print(end-start)

```

Rerun the code again you will see different excecution time because available proccessing power, computer and various variables. This is not effective way to compare. Instead, Computer Scientist compare number of the steps required for Algorithm.

For example:

```

for i in range(5):
 print(i)

f(n) = 5
```

This requires 5 steps. If you make program more complicated your equation will change.

```
count = 0

for i in range(5):
 count=+i
 print(i)

f(n)=1+2n

```

Computer Scientist call the variable n in an equation that describes the number of steps in an Algorithm the size of the problem.

The good news is , you don't care about the exact number of steps in an algorithm. We care how an algorithm performs as n gets bigger. Most inefficient algorithms will perform well if n=1. In real worls n is going to be several hundread thousand or million.

Computer Scientists use Big O notation for time and space complexity analysis.

### Constant Time Complexity

O(1) - An Algorithm run in constant time when it requires the same number of steps regardless of problem size.

````

free_books = customer[0]
T(n) = 1
````

No matter how many books are there first customer always get free book.


### Logarithmic Time Complexity

O(Log n) - Algorithms such as binary search that can discord many values at each iteration.


### Linear Time Complexity

O(n) - The linear time grows same rate as the size of the problem.


### Log Linear Time Complexity

O(n Log n) - This is a multiplication of logarithmic and linear time complexities. This algorithms often divide the data sets into smaller parts and process each peice independently.


### Quadratic Time Complexity

O(n**2) - An algorithms runs in quadratic time when its performance is directly proportional to the problem's size squared.

```
numbers = [1,2,3,4,5]

for i in numbers:
 for j in numbers:
  x = i*j
  print(x)

f(n) = 1+(1+1)n*n
f(n) = 1+2n**2
```

We will consider n**2 and ignore remaining all in order of magnitude.


### Cubic Time Complexity

O(n**3) - An algorithms runs in cubic time when its performance is directly proportional to the problem's size cubed.

```
numbers = [1,2,3,4,5]

for i in numbers:
 for j in numbers:
  for h in numbers:
   x = i+j+h 
   print(x)

f(n) = 1+(1+1+1)n**3
f(n) = 1+3n**3
```

We will consider n**2 and ignore remaining all in order of magnitude.


### Exponential Time Complexity

The honor of worst time complexity goes to the exponential time complexity. An algorithm that runs in exponential time contains a constant raised to the size of the problem.

```
Guessing a password (10**n)

pin = 931
n = len(pin)
for i in rage(10**n):
 if i==pin:
  print(i) 
```



*tip - when we are comparing two algorithms we often look at average time complecity of both.*
