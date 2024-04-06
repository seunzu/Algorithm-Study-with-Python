import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in tree:
        if i >= mid:
            sum += i - mid
    if sum < m:
        end = mid - 1
    else:start = mid + 1
print(end)