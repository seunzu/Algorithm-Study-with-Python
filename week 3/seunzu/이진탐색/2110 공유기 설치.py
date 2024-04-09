n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

start = 1
end = arr[-1] - arr[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    cur = arr[0]
    cnt = 1

    for i in range(1, n):
        if arr[i] - cur >= mid:
            cnt += 1
            cur = arr[i]
    if cnt >= c:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)


