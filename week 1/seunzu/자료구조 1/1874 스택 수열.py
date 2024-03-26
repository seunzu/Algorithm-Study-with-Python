import sys

n = int(sys.stdin.readline())

stack = []
operator = []
cur = 1

for _ in range(n):
    end = int(sys.stdin.readline())

    while cur <= end:
        stack.append(cur)
        operator.append('+')
        cur += 1

    if stack[-1] == end:
        stack.pop()
        operator.append('-')

    else:
        print("NO")
        break

else:
    for i in operator:
        print(i)
