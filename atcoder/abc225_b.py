import sys

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

c = 0
for i in range(N):
    lg = len(G[i])
    if lg == N-1:
        c += 1
    elif lg != 1:
        print("No")
        sys.exit(0)

if c == 1:
    print("Yes")
else:
    print("No")