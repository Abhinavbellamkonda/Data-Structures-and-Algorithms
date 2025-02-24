#Navie Approach
#Just try to understand
def maxPairwise():
    array = [1, 2, 3, 4, 5]
    max_pair = 0

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):  # ✅ Corrected range
            if max_pair < (array[i] * array[j]):  # ✅ Compare product of pairs
                max_pair = array[i] * array[j]

    return max_pair  # ✅ Return the max product after both loops finish
print(maxPairwise())  # Output: 20 (4 * 5)
