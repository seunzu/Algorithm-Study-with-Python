import sys
from collections import deque

n = int(sys.stdin.readline())
deque = deque()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        deque.appendleft(command[1])
    elif command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "pop_front":
        print(-1) if not deque else print(deque.popleft())
    elif command[0] == "pop_back":
        print(-1) if not deque else print(deque.pop())
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        print(1) if not deque else print(0)
    elif command[0] == "front":
        print(-1) if not deque else print(deque[0])
    elif command[0] == "back":
        print(-1) if not deque else print(deque[len(deque) - 1])