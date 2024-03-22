import sys
input = sys.stdin.readline

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

N, K = map(int, input().split())
print(comb(N, K) % 10007)
