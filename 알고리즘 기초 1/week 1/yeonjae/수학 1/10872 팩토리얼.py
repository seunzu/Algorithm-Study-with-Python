#팩토리얼로 풀기 
def factorial(n):
    if(n>1):
        return n* factorial(n-1)
    else: 
        return 1
    
ans=int(input())
print(factorial(ans))