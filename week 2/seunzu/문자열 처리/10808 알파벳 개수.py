s = list(input())
a = [0 for _ in range(26)]

for i in s:
    a[ord(i) - 97] += 1

for i in a:
    print(i, end=' ')