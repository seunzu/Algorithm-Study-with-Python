n = int(input())
for i in range(1,n+1):
    for j in range(2,n):
        print((2*i-1)*' ')
    print((n-i)*' '+'*'*(2*i-1))    

