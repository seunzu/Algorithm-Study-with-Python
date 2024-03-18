import math
n=int(input())

def lcm(a,b):
    return a*b//math.gcd(a,b)

for _ in range(n):
    a,b=list(map(int,input().split()))
    print(lcm(a,b))
