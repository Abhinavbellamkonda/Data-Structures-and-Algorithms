def gcd_eculidean(a,b):
   while b!=0:
      a,b = b, a%b
   if(b==0):
      return a

