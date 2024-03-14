import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
n, k = map(int, input().split())

for i in range(1, n + 1):
    queue.append(i)

result = []

while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

# 리스트를 문자열로 변환하여 출력
print("<" + ", ".join(map(str, result)) + ">")
