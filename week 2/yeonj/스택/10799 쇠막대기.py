pipe=input()
stack=[]
count=0

for i in range(len(pipe)):
    if pipe[i]=="(":
        stack.append("(")
    else:
        if pipe[i-1]=="(":
            stack.pop()
            count+=len(stack)
        else:
            stack.pop()
            count+=1
print(count)