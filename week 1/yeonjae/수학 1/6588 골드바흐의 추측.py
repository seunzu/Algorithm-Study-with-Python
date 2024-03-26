
#수정해야함
import sys
sys.stdin = open("input.txt", "r") # 제거
input=sys.stdin.readline

from math import sqrt
#소수 판별
def isPrime(x):
    if x==1:
        return False
    for i in range(2,int(sqrt(x)+1)):
        if(x%i==0):
            return False    
    return True

while (True):
    a=int(input())
    if a==0: break
    found=False

    for i in range(3,a):
        b=a-i
        if isPrime(i) and isPrime(b) and i%2!=0 and b%2!=0:
            found = True
            print(a, "=", i, "+", b)
            break

    if not found:
        print("Goldbach's conjecture is wrong.")