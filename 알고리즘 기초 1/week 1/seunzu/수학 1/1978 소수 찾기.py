N = int(input())
n = list(map(int, input().split()))
answer = 0

for i in n:
    count = 0

    if i == 1:
        continue

    for j in range(2, n+1):
        if i % j == 0:
            count += 1

    if count == 1:
        answer += 1

print(answer)
