import sys
input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]
stack = []
pm = [] #스택에 +,-를 기록할 것
count = 0

for i in num_list:
    while count < i: # 스택이 해당 숫자보다 작아질 때까지 .
        count += 1
        stack.append(count)
        pm.append("+")
    if stack[-1] == i: # 스택의 가장 위의 숫자가 현재 숫자와 같으면 스택에서 제거
        stack.pop()
        pm.append("-")
    else:
        print("NO")
        break
else:
    print("\n".join(pm))
