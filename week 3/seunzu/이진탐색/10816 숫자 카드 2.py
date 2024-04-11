import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
other = list(map(int, sys.stdin.readline().split()))
ans = []

card.sort()

# ver 1
for i in other:
    left = bisect_left(card, i)
    right = bisect_right(card, i)

    print(right - left, end=' ')

# ver2
# def count_by_range(arr, value):
#     right_index = bisect_right(arr, value)
#     left_index = bisect_left(arr, value)
#     return right_index - left_index
#
# for i in other:
#   print(count_by_range(card, i), end=" ")