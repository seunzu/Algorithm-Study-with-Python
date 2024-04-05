import sys
input = sys.stdin.readline

def get_cut_height(trees, target):
    total = 0
    for tree in trees:
        if tree > target:
            total += tree - target
    return total

def binary_search(trees, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cut_height = get_cut_height(trees, mid)
        if cut_height >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

n, m = map(int, input().split()) 
trees = list(map(int, input().split()))  

trees.sort()


start = 0
end = max(trees)
result = binary_search(trees, m, start, end)
print(result)
