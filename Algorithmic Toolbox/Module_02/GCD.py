#Greatest Common Division
#Here there are 2 things to remember d should be divisible by both a and b and a,b>=0
#The GCD will not be greater then min(a,b)
#Navie Approach check all possible numbers if gcd = 1 return 1 else return for in range....
#Behind the scenes calculations
'''
Find the largest number `i` that divides both 48 and 18.

Checking divisors from 1 to 18:

i = 1  (48 % 1 == 0 and 18 % 1 == 0)
i = 2  (48 % 2 == 0 and 18 % 2 == 0)
i = 3  (48 % 3 == 0 and 18 % 3 == 0)
i = 4  (48 % 4 == 0 but 18 % 4 != 0)
i = 5  (48 % 5 != 0 and 18 % 5 != 0)
i = 6  (48 % 6 == 0 and 18 % 6 == 0)  → **Largest common divisor found!**
i = 7 to 18 (None divide both numbers)

✅ **Final Answer: GCD(48, 18) = 6**

'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))
def gcd(a,b):
    if a==1 or b==1:
        return 1
    gcd_value =1
    for i in range(1,min(a,b)):
        if a%i==0 and b%i==0:
            gcd_value=i
    return gcd_value
print(gcd(a,b))

#Efficient Algorithm - Euclidean Algorithm
#gcd(a,b) = gcd(a`,b) = gcd(b,a`), where a` is the is remainder of a,b
#formula of a = bq+r => dividend = (divisor*quotient) + remainder
#In given (a,b) assume that a is greatest value and b is smallest value
#gcd(15,4)=> 15 = 4*3+0
#In Euclidean Algorithm last non zero remainder will be gcd
#We can achieve this in two ways either through recursion or iteration

#Approach1(Recursion)

def gcdEf1(a,b):
    if b==0:
        return a
    else:
        return gcdEf1(b,a%b)
print(gcdEf1(a,b))

#Approach2(Iteration)
def gcdEf2(a,b):
    while b!=0:
        a,b=b,a%b
    if(b==0):
        return a
print(gcdEf2(a,b))

