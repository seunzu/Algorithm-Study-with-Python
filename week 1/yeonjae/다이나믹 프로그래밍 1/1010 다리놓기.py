import sys
input=sys.stdin.readline
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#조합 풀어서 풀기
def comb(m, n):
    return factorial(m) // (factorial(n) * factorial(m - n))

def sites(N, M):
    return comb(M, N)

t=int(input())
for i in range(t):
    N,M=map(int,input().split())
    print(sites(N,M))
