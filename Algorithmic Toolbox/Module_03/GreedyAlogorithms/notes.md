# Greedy Algorithms - Simple Notes

## What is a Greedy Algorithm?
A greedy algorithm solves a problem by making **the best choice at each step**, without worrying about future consequences.

### Key Properties:
1. **Greedy Choice Property** - We make the best choice at each step.
2. **Optimal Substructure** - A problem can be broken into smaller subproblems, and solving each small problem optimally leads to the best global solution.

---

## Example 1: Forming the Largest Number
### **Problem**
Given a set of digits, arrange them to form the **largest possible number**.

### **Greedy Strategy**
1. Pick the **largest digit** and place it first.
2. Pick the **next largest** and place it second.
3. Repeat until all digits are used.

### **Example**
#### Input: `[9, 8, 9, 6, 1]`
#### Steps:
- Pick `9` → `9`
- Pick `9` → `99`
- Pick `8` → `998`
- Pick `6` → `9986`
- Pick `1` → `99861`

**Output:** `99861`

### **Edge Cases**
| Case | Input | Expected Output | Reason |
|------|------|----------------|--------|
| Single digit | `[5]` | `5` | Only one number available. |
| All same digits | `[3, 3, 3]` | `333` | Sorting doesn’t change order. |
| Already sorted | `[9, 8, 7]` | `987` | Algorithm should maintain order. |
| Digits with same prefix | `[9, 98, 97]` | `99897` | `98` should come before `97`. |
| Digits with zero | `[0, 0, 1]` | `100` | Non-zero should come first. |

---

## Example 2: Minimizing Total Waiting Time
### **Problem**
Given `n` patients arriving at the same time, arrange them to **minimize total waiting time**.

### **Brute Force Approach (O(n²))**
#### **Steps:**
1. Loop through all patients `n` times.
2. In each iteration, find the **patient with the shortest treatment time**.
3. Treat that patient and update waiting times for all remaining patients.

#### **Python Code:**
```python
 def min_total_waiting_time_brute_force(treatment_times):
    n = len(treatment_times)
    treated = [False] * n  # Track treated patients
    total_waiting_time = 0  

    for i in range(n):
        min_time = float('inf')
        min_index = -1

        for j in range(n):  # Find the minimum untreated patient
            if not treated[j] and treatment_times[j] < min_time:
                min_time = treatment_times[j]
                min_index = j

        treated[min_index] = True  # Mark the patient as treated
        total_waiting_time += (n - i - 1) * min_time  # Update waiting time

        # Debugging output for understanding each iteration
        print(f"Iteration {i+1}: Treat patient at index {min_index} (time {min_time}) | Waiting Time: {total_waiting_time}")
    
    return total_waiting_time

# Example Usage
times = [15, 20, 10]
print("Brute Force Total Waiting Time:", min_total_waiting_time_brute_force(times))
```

### **Iteration Breakdown:**
| **Iteration (i)** | **Find Min (Inner Loop Work)** | **Selected Patient (Min Index)** | **Waiting Patients (`n-i-1`)** | **Added to Total Wait Time** | **Updated Total Wait Time** |
|---------------------|--------------------------------|--------------------------------|------------------------------|-------------------------------|----------------------------|
| `i = 0` | Finds min from `[15, 20, 10]` → **10** | `index = 2` | `2` | `2 * 10 = 20` | `20` |
| `i = 1` | Finds min from `[15, 20]` → **15** | `index = 0` | `1` | `1 * 15 = 15` | `35` |
| `i = 2` | Finds min from `[20]` → **20** | `index = 1` | `0` | `0 * 20 = 0` | `35` |

#### **Time Complexity:** `O(n²)` (due to nested loops)

---

## **Optimized Approach (O(n log n))**
### **Steps:**
1. **Sort the treatment times in ascending order** (O(n log n)).
2. **Loop through each patient once** and update waiting times efficiently (O(n)).

#### **Python Code:**
```python
 def min_total_waiting_time_optimized(treatment_times):
    treatment_times.sort()  # Step 1: Sort in ascending order (O(n log n))
    total_waiting_time = 0
    n = len(treatment_times)

    for i in range(n):  # Step 2: Compute waiting time efficiently (O(n))
        remaining_patients = n - i - 1  # Number of patients still waiting
        total_waiting_time += remaining_patients * treatment_times[i]

        # Debugging output to understand each iteration
        print(f"Iteration {i+1}: Treat patient with time {treatment_times[i]} | Waiting Time: {total_waiting_time}")
    
    return total_waiting_time

# Example Usage
times = [15, 20, 10]
print("Optimized Total Waiting Time:", min_total_waiting_time_optimized(times))
```

### **Comparison of Brute Force vs Optimized Approach**
| Approach | Time Complexity | Why? |
|----------|---------------|------|
| **Brute Force** | **O(n²)** | Finds the minimum `n` times (nested loop). |
| **Optimized** | **O(n log n)** | Sorting first, then a single pass. |

---

## **Why Greedy Works**
- **It picks the best option at each step**.
- **It never backtracks** or changes past choices.
- **It works when the problem has an optimal substructure**.

- **Use Greedy when**: Local best choice leads to the best overall result.
- **Don't use Greedy when**: You need to try multiple possibilities to find the best one.
