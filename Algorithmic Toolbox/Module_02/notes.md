## **Fibonacci Sequence**
What is **Fibonacci**?
- The Fibonacci sequence is a series of numbers where each number is the sum of the two previous numbers.

#### **Fibonacci Series**

- 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …
- Starts with 0 and 1
- Each next number is the sum of the two before it.

- **Fibonacci Formula**
- F(n)=F(n−1)+F(n−2)
- F(0) = 0
- F(1) = 1
- F(2) = 1 (0 + 1)
- F(3) = 2 (1 + 1)
- F(4) = 3 (1 + 2)
- F(5) = 5 (2 + 3)

#### Fibonacci Using Recursion (Slow Method)

```
python

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```
print(fibonacci(10))  # Output: 55
Problem: Very slow for large numbers because it repeats calculations.

Fastest Fibonacci Using Iteration

```
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
```
- print(fibonacci_iterative(10))  # Output: 55
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) (No extra memory needed!)

---

## **Greatest Common Divisor (GCD)**
What is **GCD**?
- The Greatest Common Divisor (GCD) of two numbers is the largest number that divides both numbers exactly.

**Examples**
```
GCD(12, 18) = 6  (because 6 is the biggest number that divides both 12 and 18)
GCD(48, 18) = 6
GCD(56, 98) = 14
GCD(101, 103) = 1  (because 101 and 103 are prime numbers)
```
Naïve GCD Method (Slow)
```
Step-by-step Explanation
Find the smaller number of a and b.
Check every number from 1 to min(a, b).
Find the largest number that divides both.
Example: GCD(48, 18)
Divisors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48
Divisors of 18: 1, 2, 3, 6, 9, 18
Common Divisors: 1, 2, 3, 6
Largest common divisor = 6
```


```
python 

def naive_gcd(a, b):
    gcd_value = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i  # Update the largest divisor
    return gcd_value
```
- print(naive_gcd(48, 18))  # Output: 6
- Problem: Slow for large numbers because it checks every number up to min(a, b).

**Efficient GCD**: 
- Euclidean Algorithm (Fast)
- Instead of checking all numbers, the Euclidean Algorithm reduces the problem step by step.

- gcd(a,b)=gcd(b,a mod b)
- Keep replacing a with b and b with a % b until b = 0.
The last a value is the GCD.
```
Step-by-Step Example: 
GCD(48, 18)
       = gcd(18, 48 % 18)
       = gcd(18, 12)   (48 % 18 = 12)

       = gcd(12, 18 % 12)
       = gcd(12, 6)    (18 % 12 = 6)

       = gcd(6, 12 % 6)
       = gcd(6, 0)     (12 % 6 = 0)

       GCD = 6
```

```
python 

def gcd_euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```
- print(gcd_Euclidean(48, 18))  # Output: 6
- Time Complexity: O(log(min(a, b)))
- Much faster than the naïve method

---

## **Computing Runtime**

### **The Problem with Measuring Runtime Using Lines of Code**

Initially, we might think counting lines of code is a good way to measure runtime. However, this is inaccurate because:

- **Different operations take different amounts of time.**  
  - Example: Assigning a variable (`x = 5`) is **faster** than allocating an array in memory.
- **Hardware differences matter.**  
  - A **supercomputer** will run the same program **faster** than a phone.
- **Memory allocation impacts performance.**  
  - If an array is allocated in **cache**, it’s **fast**; if it uses **RAM** or **disk**, it's **slower**.
- **Compilers optimize code differently.**  
  - The same program may execute **differently** based on how it's compiled.

---

### **Fibonacci Number Calculation Example**

We analyze a simple Fibonacci number calculation algorithm:

```
python

def fibonacci(n):
    fib = [0] * (n + 1)  # Create an array
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]  # Compute Fibonacci numbers
    
    return fib[n]  # Return the nth Fibonacci number
```

Now, let’s break down each part of the algorithm.

#### **Step 1: Array Initialization**
```
python
fib = [0] * (n + 1)
```
- Allocates an **array** of size `n+1`.
- Might require **searching for memory space**.
- May involve **zeroing out the memory** (depends on system).

#### **Step 2: Assignments**

```
python

  fib[0] = 0
  fib[1] = 1
```
- At the **machine level**, this involves:
  - **Loading a pointer**.
  - **Performing pointer arithmetic**.
  - **Storing a value in memory**.

#### **Step 3: Loop Execution**
```
python

for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
```
**Operations inside the loop:**
- **Increment `i`**
- **Compare `i` to `n`**
- **Look up two array values**
- **Perform addition**
- **Store the result**

---

### **Visualizing Execution Flow**

#### **Memory Allocation in Array Creation**
```
Memory: |____|____|____|____|____|____|
Index:    0    1    2    3    4    5  
```
After initialization:
```
Memory: |  0 |  1 |  ?  |  ?  |  ?  |  ?  |
Index:    0    1    2    3    4    5  
```
After running the loop:
```
Memory: |  0 |  1 |  1  |  2  |  3  |  5  |
Index:    0    1    2    3    4    5  
```

### **Loop Execution in Steps (Tree Representation)**
Each Fibonacci number depends on the sum of the previous two:
```
        fib(5)
       /      \
   fib(4)    fib(3)
   /    \      /    \
fib(3)  fib(2) fib(2) fib(1)
```
For `n=5`, **each call depends on previous results**.

---

### **Why Counting Lines of Code Fails**

#### **Different lines take different times to execute.**
- `fib[i] = fib[i-1] + fib[i-2]` → involves **memory lookup + arithmetic**.
- `fib[0] = 0` → simple assignment.
- **These are not equal in execution time!**

#### **System-dependent factors:**
- **Faster on a supercomputer** than a phone.
- If stored in **cache**, **faster** than **RAM** or **disk**.

#### **Recursive Fibonacci is even worse!**
- Uses a **tree-like call structure**, leading to **exponential growth**.

### **Real Issues in Runtime Calculation**
We want to measure **actual runtime**, but:
- **We don’t know what computer it will run on.**
- **Different computers have different speeds.**
- **Compiler optimizations change how code runs.**

### **A Better Approach**
Instead of measuring **exact time**, we **measure growth rate**.

#### **Real-World Examples of Growth Rate (Big-O Notation)**
- Instead of measuring the exact time an algorithm takes, we analyze how its runtime increases as the input size **(n)** grows. This is called Time Complexity and is measured using Big-O Notation.
- Think of it like traffic on a road—as more cars (data) are added, some roads handle the traffic better than others.

## **Asymptotic Notation (Big-O Notation) - Simple Notes**

### **Why Do We Need Asymptotic Notation?**
Computing exact runtimes is **hard** because:
- Different computers have **different speeds**.
- **System architecture** affects how operations are performed.
- **Memory hierarchy** (cache, RAM, disk) impacts execution time.
- **Compiler optimizations** change how code runs.

We need a way to **compare algorithms** without worrying about small details. **Asymptotic notation** helps us measure how an algorithm’s runtime grows as input size (`n`) increases.

---

### **Ignoring Constant Multiples**
- Some factors affect runtime by a **constant multiple** (e.g., a faster CPU reduces time but does not change growth rate).
- If one system is **100 times faster**, it still follows the **same runtime pattern**.
- Example:
  - **Algorithm 1** runs in **n** time.
  - **Algorithm 2** runs in **100n** time.
  - When `n` is **very large**, both still grow similarly.
  
So, we **ignore constant multiples** and focus on **how the function scales with `n`**.

---

### **Asymptotic Growth - How Runtime Scales with Input Size**
Instead of exact runtimes, we check **how runtime increases** as `n` grows:
- **O(n):** Linear growth (proportional to input size).
- **O(n log n):** Log-linear growth (used in efficient sorting algorithms).
- **O(n²):** Quadratic growth (much slower as `n` increases).
- **O(2ⁿ):** Exponential growth (becomes impossible for large `n`).

##### **Example: Comparing Growth Rates**
| Complexity  | Input Size `n` = 1M | Time Needed |
|------------|-----------------|---------|
| **O(n)**  | 1,000,000 | Fast  |
| **O(n log n)** | ~30,000,000 | Slower |
| **O(n²)** | 30,000,000,000 | Very Slow |
| **O(2ⁿ)** | `n = 50` → 2 weeks! | Impossible |

**Tips:**
- **O(n) and O(n log n) can handle big inputs.**
- **O(n²) struggles with large inputs.**
- **O(2ⁿ) is impractical for large `n`.**

---
#### **Simple Examples for Each Complexity**
##### **O(1) - Constant Time**
**Real-World Example:** Taking one cookie from a jar.
```python
def get_first_item(arr):
    return arr[0]
```
**Explanation:** No matter how big `arr` is, it always takes the same time to get the first item.

##### **O(log n) - Logarithmic Time**
**Real-World Example:** Finding a word in a dictionary.
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
**Explanation:** Each time, we cut the problem in half, making it much faster than checking every item.

##### **O(n) - Linear Time**
**Real-World Example:** Blowing up balloons one at a time.
```python
def find_item(arr, target):
    for item in arr:
        if item == target:
            return True
    return False
```
**Explanation:** If we have `n` items, we might have to check all `n` one by one.

##### **O(n log n) - Log-Linear Time**
**Real-World Example:** Sorting books in a library using categories first.
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
**Explanation:** Sorting is done in a smart way by first splitting the list, then sorting and merging back.

##### **O(n²) - Quadratic Time**
**Real-World Example:** Every student in a class shaking hands with every other student.
```python
def all_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])
```
**Explanation:** For every item, we check every other item, making it much slower as `n` grows.

##### **O(2ⁿ) - Exponential Time**
**Real-World Example:** Doubling the number of puzzle pieces every step.
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```
**Explanation:** Every new step doubles the work, making it impossible to handle for large `n`.


#### **Tips**
- Instead of measuring exact runtime, we measure **how runtime grows as input size increases**.  
- **Big-O notation helps compare algorithms fairly**, regardless of hardware.
- **For large inputs, picking the right algorithm makes a huge difference**.  
- **Best Choices:** O(1) → O(log n) → O(n) → O(n log n)  
- **Avoid if possible:** O(n²) → O(2ⁿ) 

---

## **Big-O Notation**

### **What is Big-O Notation?**
Big-O notation helps us understand **how an algorithm’s runtime grows** as the input size (`n`) increases. Instead of measuring exact time, we **focus on how fast the number of steps increases**.

For example:
- **Checking one paper in a pile of `n` papers** → `O(n)`
- **Comparing every paper with every other paper** → `O(n²)`
- **Splitting the pile in half each time** → `O(log n)`

### **Why Use Big-O?**
1. **It helps compare algorithms fairly**
   - `O(n²)` grows **much faster** than `O(n)`, so we know which one is better for large inputs.

2. **It simplifies complex formulas**
   - Instead of writing `3n² + 5n + 2`, we just write `O(n²)`.

3. **It ignores computer speed**
   - Whether on a **fast** or **slow** computer, Big-O remains the same.

#### **Simple Examples**

| **Big-O Notation**  | **Real-World Example** | **Steps as `n` Grows** |
|---------------------|------------------------|-----------------|
| **O(1) - Constant Time**  | Taking one book from a shelf | Always the same |
| **O(log n) - Logarithmic Time**  | Searching for a word in a dictionary | Grows slowly |
| **O(n) - Linear Time**  | Checking every book one by one | Grows evenly |
| **O(n log n) - Log-Linear Time**  | Sorting books by dividing groups first | Grows moderately |
| **O(n²) - Quadratic Time**  | Comparing every book with every other book | Grows very fast |
| **O(2ⁿ) - Exponential Time**  | Doubling puzzle pieces each step | Grows impossibly fast |

### **Big-O Limitations**
- **It ignores constants**: `O(2n)` and `O(n)` are treated the same, even though `2n` is twice as slow.
- **It only cares about large inputs**: Sometimes a slower Big-O is faster for small numbers.
- 
### **Basic Rules of Big-O (Explained Clearly)**

### **Ignore Constants**
 - **Example:** `O(7n³) = O(n³)` 
 - **Example:** `O(n² / 3) = O(n²)`  
 **Why?** Because **multiplying by a constant** does not change how fast a function grows.

Imagine two runners:
- **Person A starts 7 steps ahead.**
- **Person B runs 3 times faster.**
- Over long distances, **Person B still wins**, and the 7 steps don’t matter!


### **Keep the Largest Exponent**
- **Example:** `O(n² + n) = O(n²)` 
- **Example:** `O(n⁴ + n³ + n) = O(n⁴)`
- **Why?** The highest power of `n` dominates growth.

Imagine two people growing at different rates:
- **Person A grows 2 cm per year (`n²`).**
- **Person B grows 1 cm per year (`n`).**
- In `10 years`, Person A has grown **100 cm**, while Person B has grown only **10 cm**. 
- **Person A’s growth dominates!**

### **Exponential Growth Beats Polynomial Growth**
- **Example:** `O(n⁵) < O(2ⁿ)` 
- **Example:** `O(n¹⁰⁰) < O(1.1ⁿ)`
**Why?** Exponential functions grow much faster than polynomials.

Imagine you get:
- **$5 every year (`n⁵`)** → Slow growth.
- **Your money doubles every year (`2ⁿ`)** → Fast growth!
- By `Year 20`, doubling is much bigger than adding $5 every year!


### **Logarithms Grow the Slowest**
- **Example:** `O(log³ n) < O(√n)`
- **Example:** `O(n log n) < O(n²)`
**Why?** Logarithmic functions **increase very slowly** compared to `n`.

Think of **searching a dictionary**:
- **Checking every word one by one (`O(n)`)** is slow.
- **Flipping pages in half (`O(log n)`)** is much faster!


### **Drop Lower Order Terms**
- **Example:** `O(n² + n) = O(n²)` 
- **Example:** `O(2ⁿ + n⁹) = O(2ⁿ)`
**Why?** When adding two terms, the one that **grows the fastest** is the only one that matters.

Imagine two trains:
- **Train A speeds up every second (`n²`).**
- **Train B moves at constant speed (`n`).**
- After `n=100`, Train A moves **10,000 km**, while Train B moves only **100 km**.
- **Train A dominates, so we ignore Train B.**

### **Applying Big-O to a Real Algorithm**
Let’s analyze a **Fibonacci Algorithm**:
```python
def fibonacci(n):
    fib = [0] * (n + 1)  # Allocate memory → O(n)
    fib[0], fib[1] = 0, 1  # Assign values → O(1)
    
    for i in range(2, n + 1):  # Loop n-1 times → O(n)
        fib[i] = fib[i - 1] + fib[i - 2]  # Addition operation → O(n) (large numbers)
    
    return fib[n]  # Return result → O(1)
```
### **Step-by-Step Big-O Breakdown**
| **Operation** | **Big-O Complexity** |
|--------------|---------------------|
| **Allocate Array** (`O(n)`) | Every element is initialized |
| **First Two Assignments** (`O(1)`) | Simple constant-time operations |
| **Loop Iterations** (`O(n)`) | Runs `n-1` times |
| **Adding Two Numbers** (`O(n)`) | Large numbers take `O(n)` time to add |
| **Final Return Statement** (`O(1)`) | Constant-time operation |

### **Final Complexity:**
- **Loop runs `O(n)` times.**  
- **Each loop iteration does `O(n)` work (big number addition).**  
- **Total:** `O(n) * O(n) = O(n²)`

**Conclusion: This algorithm runs in `O(n²)`, which is slow!**

### **Summary of Big-O Simplifications**
| **Rule**                  | **Example Before**   | **Example After**  | **Why?** |
|---------------------------|---------------------|-------------------|----------|
| **Ignore constants**      | `O(5n³)`             | `O(n³)`            | Constants don’t matter |
| **Largest exponent wins** | `O(n² + n)`         | `O(n²)`            | Higher power dominates |
| **Exponential beats polynomial** | `O(n⁵)` vs. `O(2ⁿ)`  | `O(2ⁿ)` | Exponential grows faster |
| **Logs grow slowest**     | `O(n log n)` vs. `O(n²)` | `O(n²)` | Logarithm is slowest |
| **Drop lower terms**      | `O(n² + n)`         | `O(n²)`            | Lower-order terms are negligible |


### **Summary**
- **Big-O focuses on the fastest-growing term.**  
- **Constants and smaller terms don’t matter.**  
- **Exponential functions grow much faster than polynomials.**  
- **Logarithmic functions grow the slowest.**
- **Big-O describes how fast an algorithm grows as input increases.**
- **It helps us choose better algorithms for large inputs.**
- **It ignores small details to focus on growth patterns.**


