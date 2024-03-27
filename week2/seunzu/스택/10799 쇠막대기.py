ir = list(input())
stack = []
count = 0

for i in range(len(ir)):
    if ir[i] == '(':
        stack.append('(')
    else:
        if ir[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)