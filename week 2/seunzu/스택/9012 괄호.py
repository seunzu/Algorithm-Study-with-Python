t = int(input())

for _ in range(t):
    ps = input()
    stack = []

    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break

    else:
        if stack:
            print("NO")
        else:
            print("YES")