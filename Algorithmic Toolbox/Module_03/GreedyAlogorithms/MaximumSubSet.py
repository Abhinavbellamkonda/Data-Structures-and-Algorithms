from itertools import combinations

def max_subset_sum(numbers, limit):
    best_limit=0
    best_subset = []
    for r in range(1, len(numbers) +1):     # r=1,2,3,4,5
        for combo in combinations(numbers, r):
            total_limit = sum(combo)
            if total_limit <= limit and total_limit > best_limit:
                best_limit = total_limit
                best_subset = combo
    return best_subset, best_limit


numbers = [10, 20, 30, 40, 50]
limit = 70
print(max_subset_sum(numbers, limit))