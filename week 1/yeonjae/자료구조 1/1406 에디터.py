import sys
left_stack = list(input())
stack = int(input())
right_stack = []

cursur = len(left_stack)
for i in range(stack):
    command = sys.stdin.readline().split()

    if(command[0] == 'L'):
        if(left_stack != []):
            right_stack.append(left_stack.pop())

    if(command[0] == 'D'):
        if(right_stack != []):
            left_stack.append(right_stack.pop())

    if(command[0] == 'B'):
        if(left_stack):
            left_stack.pop()

    if(command[0] == 'P'):
        left_stack.append(command[1])

print(''.join(left_stack),end='')
print(''.join(list(reversed(right_stack))),end='')