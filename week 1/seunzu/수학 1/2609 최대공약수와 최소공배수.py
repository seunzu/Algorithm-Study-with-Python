# import math

n, m = map(int, input().split())

# ver 1
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# ver 2
# math.gcd

# ver 1
def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

# ver 2
# def lcm(a, b):
#     return a * b / math.gcd(a, b)

# ver 3
# math.lcm(a, b)

print(gcd(n, m))
print(lcm(n, m))




