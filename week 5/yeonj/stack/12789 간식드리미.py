from collections import deque
import sys
input=sys.stdin.readline

n=int(input())

queue=deque(map(int,input().split()))
waiting=list()
stack=list()
order=1

while True:
    if order>n:break
    elif len(stack)>0 and stack[-1]==order:
        tmp=stack.pop()
        waiting.append(tmp)
        order+=1

    elif len(queue)>0 and queue[0]==order:
        this=queue.popleft()
        waiting.append(this)
        order+=1
    elif len(queue)>0:
        this=queue.popleft()
        stack.append(this)
    else:break

ans=[i for i in range(1,n+1)]
if waiting==ans:
    print("Nice")
else:
    print("Sad")