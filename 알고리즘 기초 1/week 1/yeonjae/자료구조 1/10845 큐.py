import sys
from collections import deque
input=sys.stdin.readline
queue=deque()
n=int(input())
for i in range(n):
    word=input().split()
    if word[0]=="push":
        queue.append(word[1])
    elif word[0]=="pop":
        if queue:
            print(queue.popleft())
        else: 
            print(-1)
    elif word[0]=="size":
        print(len(queue))
    elif word[0]=="empty":
        if queue:
            print(0)
        else: print(1)
    elif word[0]=="front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif word[0]=="back":
        if queue:
            print(queue[-1])
        else: print(-1)


