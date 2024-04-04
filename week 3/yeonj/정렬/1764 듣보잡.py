import sys
input = sys.stdin.readline
a, b = map(int, input().split())

nohear = set()
nosee = set()

for _ in range(a):
    nohear.add(input().strip())  

for _ in range(b):
    nosee.add(input().strip())  

intersection = nohear & nosee

print(len(intersection))
for name in sorted(intersection):  
    print(name)
