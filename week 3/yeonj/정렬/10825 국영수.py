import sys
input=sys.stdin.readline
score=[]
n=int(input())
for i in range(n):
    name,k,e,m=input().split()
    score.append((name,int(k),int(e),int(m)))

score.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in score:
    print(i[0])