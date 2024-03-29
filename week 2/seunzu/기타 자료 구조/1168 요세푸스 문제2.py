# 세그먼트 트리
# => 시간 초과(Python3) -> PyPy3으로 제출
from sys import stdin

input = stdin.readline()

# 세그먼트 트리 초기화, 재귀적으로 호출
# 입력으로 받은 구간에 대한 세그먼트 트리 만듦
# 각 노드 = 해당하는 구간의 요소 수
def init(tree, node, start, end):
    if start == end:
        tree[node] = 1
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(tree, node * 2, start, mid) + init(tree, node * 2 + 1, mid + 1, end)

    return tree[node]

# 세그먼트 트리 업데이트
# dellete -> 세그먼트 트리에서 빼는 역할
# 해당 값의 위치를 찾아가며 트리의 각 노드에 있는 값 감소
def update(tree, node, start, end, dellete):
    tree[node] -= 1
    if start == end:
        return 0
    else:
        mid = (start + end) // 2
        if dellete <= mid:
            return update(tree, node * 2, start, mid,dellete)
        else:
            return update(tree, node * 2 + 1, mid + 1, end, dellete)

# 세그먼트 트리 쿼리
# 주어진 순서에 해당하는 요소 찾음
# 구간 트리 순회하면서 각 노드에 저장된 값과 주어진 순서 비교하여 올바른 위치 찾음
def query(tree, node, start, end, order):
    if start == end:
        return start

    mid = (start + end) // 2

    if order <= tree[node * 2]:
        return query(tree, node * 2, start, mid, order)
    else:
        return query(tree, node * 2 + 1, mid + 1, end, order - tree[node * 2])


n, k = map(int, input.split())
tree = [0] * 3000000
init(tree, 1, 1, n)
index = 1
array = []

for i in range(n):
    size = n - i
    index += k - 1

    if index % size == 0:
        index = size
    elif index > size:
        index %= size

    num = query(tree, 1, 1, n, index)

    update(tree, 1, 1, n, num)
    array.append(str(num))

print("<", ", ".join(array), ">", sep='')