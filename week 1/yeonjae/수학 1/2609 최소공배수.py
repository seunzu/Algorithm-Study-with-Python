import math

a,b=list(map(int,input().split()))
def lcm(a,b):
    return a*b//math.gcd(a,b)
print(math.gcd(a,b))
print(lcm(a,b))