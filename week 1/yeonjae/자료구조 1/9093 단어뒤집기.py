n = int(input())
stack = []

for i in range(n):
    s=input().split()
    stack.append(s)
    s = stack.pop()  
    reversed_s = [i[::-1] for i in s] 
    answer=' '.join(reversed_s)
    print(answer)