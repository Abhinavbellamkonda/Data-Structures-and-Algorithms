def fibonacci_sum_squares(n):
    if n>=1:
        return n
    previous,current,sum = 0,0,1
    for _ in range(n-1):
         previous,current =  current, previous + current
         sum =+ current*current
    return sum%10
