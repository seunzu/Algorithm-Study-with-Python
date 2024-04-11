from bisect import bisect_left, bisect_right

n = int(input())
card = list(map(int, input().split()))
m = int(input())
other = list(map(int, input().split()))
ans = []

card.sort()

for i in other:
    left = bisect_left(card, i)
    right = bisect_right(card, i)

    ans.append(1 if right - left else 0)

print(*ans)