import sys
input=sys.stdin.readline
n=int(input())
regis=[]
for i in range(n):
    age,name=input().split()
    regis.append((int(age),name))

regis.sort(key=lambda x:int(x[0]))
for i in regis:
    print(i[0],i[1])