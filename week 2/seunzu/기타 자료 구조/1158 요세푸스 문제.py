from collections import deque

n, k = map(int, input().split())
dq = deque()
answer = []

for i in range(1, n+1): dq.append(i)

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())

    answer.append(dq.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))
