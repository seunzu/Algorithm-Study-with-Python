t = int(input())

for _ in range(t):
    str = list(input().split())
    for j in str:
        print(j[::-1], end=' ')