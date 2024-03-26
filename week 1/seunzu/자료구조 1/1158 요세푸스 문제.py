from collections import deque

N, K = map(int, input().split())

dq = deque()
answer = []


for i in range(1, N + 1):
    dq.append(i)

while dq:
  for _ in range(K - 1):
    dq.append(dq.popleft())

  answer.append(dq.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))