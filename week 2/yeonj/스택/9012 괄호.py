import sys
n=int(input())

for i in range(n):
    stack=[]
    s=input()
    for j in s:
        if j=="(":
            stack.append(j);
        elif j==")":
            if stack:
                stack.pop()
            else: print("NO")
            break
    else:
        if stack:print("NO")
        else:print("YES")
