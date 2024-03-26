import sys
input=sys.stdin.readline

from math import sqrt

def isPrime(x):
    if x==1:
        return False
    for i in range(2,int(sqrt(x)+1)):
        if(x%i==0):
            return False    
    return True

a,b=list(map(int,input().split()))
for i in range(a,b+1):
    if isPrime(i):
        print(i)