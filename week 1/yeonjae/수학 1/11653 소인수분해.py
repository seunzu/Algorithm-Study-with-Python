import sys
input=sys.stdin.readline
n = int(input())
i = 2
factors = []
while i <= n:
    if n % i == 0:
        factors.append(i)
        n = n // i  
    else:
        i = i + 1
for factor in factors: 
    print(factor)
