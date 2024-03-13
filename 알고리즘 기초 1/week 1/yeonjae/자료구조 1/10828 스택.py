import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    sen = sys.stdin.readline().split()

    if sen[0] == "push":
        stack.append(sen[1])
    elif sen[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif sen[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif sen[0] == "size":
        print(len(stack))
    elif sen[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
