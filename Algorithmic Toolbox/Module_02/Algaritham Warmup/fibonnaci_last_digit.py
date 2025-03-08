def fibonnaci_last_digit(n):
    if n <= 1:
        return n                                                     #O(1)

    previous = 0
    current = 1

    for _ in range(n-1):
        previous, current = current, previous + current              #O(N)

    return current%10


#O(N^2)