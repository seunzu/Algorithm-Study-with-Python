import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.insert(0, command[1])
    elif command[0] == 'pop':
        print(-1) if len(queue) == 0 else print(queue.pop())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1) if len(queue) == 0 else print(0)
    elif command[0] == 'front':
        print(-1) if len(queue) == 0 else print(queue[len(queue) - 1])
    elif command[0] == 'back':
        print(-1) if len(queue) == 0 else print(queue[0])
