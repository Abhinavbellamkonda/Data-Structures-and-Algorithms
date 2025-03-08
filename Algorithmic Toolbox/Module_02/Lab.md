# Big-O Notation: Plots

# **Big-O Notation: Growth Rate Visualization**
This notebook visualizes how different functions grow, helping us understand **algorithm complexity**.

## **Definitions**
Consider two functions **f(n)** and **g(n)** that take non-negative real values for all positive integers.

- **f grows slower than g** (denoted as **f ≺ g**)  
  If the ratio **f(n)/g(n) → 0** as **n → ∞**.
- **f grows no faster than g** (denoted as **f ⪯ g**)  
  If there exists a constant **c** such that:  
  **f(n) ≤ c ⋅ g(n)** for all large **n**.

**Important Notes**
- **f ≺ g** is the same as **f = o(g)** (small-o notation).
- **f ⪯ g** is the same as **f = O(g)** (Big-O notation).
- Both **5n² = O(n³)** and **5n² = O(n²)** are true because **5n²** grows **no faster** than **n²** and **n³**.
- If **x = 2**, then both **x ≤ 2** and **x ≤ 3** are correct.

**🔹 Plotting: Two Simple Examples**
Let's start by loading the necessary **Python libraries**.

```
python

# Load Libraries
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
```

**Example 1: Comparing Two Growth Rates**
We visualize that **20n grows slower than 7n² + 6n + 5**.

```
python

n = np.linspace(1, 100)
plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
plt.plot(n, 20 * n, label="20n")
plt.legend(loc='upper left')
plt.show()
```

**Common Rules of Growth Rate Comparison**
### **Multiplicative Constants Can Be Ignored**
- **c ⋅ f ⪯ f**
- Examples: **5n² ⪯ n²**, **n²/3 ⪯ n²**.

### **Out of Two Polynomials, the One with Larger Degree Grows Faster**
- **nᵃ ⪯ nᵇ** for **0 ≤ a ≤ b**.
- Examples: **n ≺ n²**, **√n ≺ n²/3**, **n² ≺ n³**.

### **Any Polynomial Grows Slower than Any Exponential**
- **nᵃ ≺ bⁿ** for **a ≥ 0, b > 1**.
- Examples: **n³ ≺ 2ⁿ**, **n¹⁰⁰ ≺ 1.1ⁿ**.

### **Any Polylogarithm Grows Slower than Any Polynomial**
- **(log n)ᵃ ≺ nᵇ** for **a, b > 0**.
- Examples: **(log n)³ ≺ √n**, **n log n ≺ n²**.

### **Smaller Terms Can Be Omitted**
- If **f ≺ g**, then **f + g ⪯ g**.
- Examples: **n² + n ⪯ n²**, **2ⁿ + n⁹ ⪯ 2ⁿ**.

## **Visualizing These Growth Comparisons**
### **Rule 5: Smaller Terms Can Be Omitted**
```
python

n = np.linspace(1, 100)
plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
plt.plot(n, 7 * n * n, label="7n^2")
plt.legend(loc='upper left')
plt.show()
```

### **Rule 2: Out of Two Polynomials, the One with Larger Degree Grows Faster**
```
python

n = np.linspace(1, 100)
plt.plot(n, n, label="n")
plt.plot(n, n * n, label="n^2")
plt.plot(n, n * n * n, label="n^3")
plt.legend(loc='upper left')
plt.show()
```

### **Rule 3: Any Polynomial Grows Slower than Any Exponential**
```
python

n = np.linspace(1, 20)
plt.plot(n, n ** 4, label="n^4")
plt.plot(n, 2 ** n, label="2^n")
plt.legend(loc='upper left')
plt.show()
```

### **Rule 4: Any Polylogarithm Grows Slower than Any Polynomial**
```
python

n = np.linspace(1, 100)
plt.plot(n, n ** 0.5, label="n^.5")
plt.plot(n, np.log(n) ** 3, label="(log n)^3")
plt.legend(loc='upper left')
plt.show()
```

### **Final Exercise: Find Where \( n^{0.1} \) Becomes Larger Than \( (\log n)^5 \)**
```
python

n = np.linspace(1, 10000**50)
plt.plot(n, n ** 0.1, label="n^.1", linestyle='dashed')
plt.plot(n, (np.log(n) ** 5), label="(log n)^5", linestyle='solid')
plt.legend(loc='upper left')
plt.xlabel("n")
plt.ylabel("Growth")
plt.title("Comparison of n^0.1 vs (log n)^5")
plt.show()
```

# **Logarithm Rules for Algorithm Analysis**

## **Logarithm Properties and Examples**

| **Rule** | **Formula** | **Example** |
|----------|------------|------------|
| **Log of an exponent** | \\( \\log_a (n^k) = k \\log_a n \\) | \\( \\log_2 (8^3) = 3 \\log_2 8 = 9 \\) |
| **Log of a product** | \\( \\log_a (n \\cdot m) = \\log_a n + \\log_a m \\) | \\( \\log_2 (8 \\times 4) = 3 + 2 = 5 \\) |
| **Log of a power** | \\( n \\log_a b = b \\log_a n \\) | \\( 5 \\log_2 3 = 3 \\log_2 5 \\) |
| **Change of base** | \\( \\log_a n \\cdot \\log_b a = \\log_b n \\) | \\( \\log_2 10 \\times \\log_{10} 2 = 1 \\) |

## **Why Are Logarithm Rules Useful?**
- Logarithms appear when **problems are repeatedly divided into smaller parts** (Binary Search, Merge Sort, Recursion).
- They help estimate **how many times we divide an input** before it becomes trivial.
- The rules simplify logarithmic expressions **when analyzing complexity**.

---
