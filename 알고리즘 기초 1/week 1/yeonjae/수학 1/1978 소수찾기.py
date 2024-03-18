from math import sqrt 
def isPrime(x):
    if x==1:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    return  True


n=int(input())
a=list(map(int,input().split()))
count=0
for i in a:
    if isPrime(i):
        count+=1

print(count)       