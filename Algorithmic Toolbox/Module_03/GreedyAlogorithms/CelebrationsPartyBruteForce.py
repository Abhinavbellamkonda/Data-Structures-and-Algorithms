from itertools import combinations


def brute_force_max_enjoyment(guests, budget):
    best_enjoyment = 0
    best_combination = []

    # Try all possible group sizes (1 guest, 2 guests, ... all guests)
    for r in range(1, len(guests) + 1):
        for combo in combinations(guests, r):  # Generate all subsets of r guests
            total_cost = sum(guest[2] for guest in combo)  # Sum of costs
            total_enjoyment = sum(guest[1] for guest in combo)  # Sum of enjoyment

            print(f"Checking combination: {combo}, Cost: {total_cost}, Fun: {total_enjoyment}")  # Debugging

            if total_cost <= budget and total_enjoyment > best_enjoyment:
                best_enjoyment = total_enjoyment
                best_combination = combo  # Save best combination

    return [guest[0] for guest in best_combination], best_enjoyment  # Return guest names & max fun


# Example usage
guests = [
    ("Alice", 80, 50),
    ("Bob", 60, 30),
    ("Charlie", 100, 70),
    ("David", 50, 20),
    ("Eve", 90, 60)
]

budget = 100

print(brute_force_max_enjoyment(guests, budget))  # Call function and print result
