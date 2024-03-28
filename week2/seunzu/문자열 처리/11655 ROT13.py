s = input()
answer = []

for i in s:
    if 'A' <= i <= 'Z':
        answer.append(chr((ord(i) - ord('A') + 13) % 26 + ord('A')))
    elif 'a' <= i <= 'z':
        answer.append(chr((ord(i) - ord('a') + 13) % 26 + ord('a')))
    else:
        answer.append(i)

print(''.join(answer))
