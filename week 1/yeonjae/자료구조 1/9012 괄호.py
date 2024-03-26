n=int(input())
#( push로 넣고 ) 만났을때 pop으로 빼기 
for i in range(n):
    sen=input()
    stack=[]
    for j in sen:
        if j=="(":
            stack.append(j)
        elif j==")":
            if stack:
                stack.pop()
            else:
                print("NO")
    else:
        if stack:print("NO")
        else: print("YES")