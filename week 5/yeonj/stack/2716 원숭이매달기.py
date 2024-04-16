import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    tree = input().strip()
    stack = []
    count = 0

    if not tree:  # 덩굴이 비어있는 경우
        print(1)
        continue

    for j in tree:
        if j == "[":
            stack.append(j)
        elif j == "]":
            if stack:
                stack.pop()
                count += 1
            else:
                count += 1
                break

    else:
        count += len(stack)

    print(count*2)
