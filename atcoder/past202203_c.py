from collections import deque

a = deque(list(input()))
c = 0
while len(a) >= 4:
    a.pop()
    a.pop()
    a.pop()
    c += 1

a.append(chr(c+96))

print("".join(a))
