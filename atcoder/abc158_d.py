from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

S = deque(input())
Q = int(input())
rev = False
for _ in range(Q):
    t, *q = input().split()
    if t == "1":
        rev = not rev
    else:
        f, c = q
        if f == "1":
            if rev:
                S.append(c)
            else:
                S.appendleft(c)
        else:
            if rev:
                S.appendleft(c)
            else:
                S.append(c)
    # print(S, rev)

if rev:
    print("".join(reversed(S)))
else:
    print("".join(S))
