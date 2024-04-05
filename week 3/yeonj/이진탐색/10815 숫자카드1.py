def binary_search(cards, target):
    left = 0
    right = len(cards) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == target:
            return 1
        elif cards[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(input())
cards = list(map(int, input().split()))
cards.sort()  

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(binary_search(cards, target), end=" ")
