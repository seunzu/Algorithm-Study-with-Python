import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))

# 두 포인터 설정
left, right = 0, 0
sum = 0
count = 0

while True:
    if sum >= m:
        sum -= a[left]
        left += 1
    elif right == n:
        break
    else:
        sum += a[right]
        right += 1

    if sum == m:
        count += 1

print(count)