n=int(input())

for j in range(n,0,-1):
    print((n-j)*' '+'*'*(2*j-1))
for i in range(2,n+1):
    print((n-i)*' '+'*'*(2*i-1))    