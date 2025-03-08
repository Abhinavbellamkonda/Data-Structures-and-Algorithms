def gcd(a, b):
    current_gcd = 1
    for i in range(2, min(a,b) +1):
        if a%i==0 and b%i==0:
            if i>current_gcd:
                current_gcd=1
    
    return current_gcd
