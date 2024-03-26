# ver 1
import sys
print(sys.stdin.read())

# ver 2
while True:
    try:
        print(input())
    except EOFError:
        break