from collections import defaultdict

N = int(input())
d = defaultdict(lambda: 0)
for _ in range(N):
    d[input()] += 1

name = ""
cnt = 0
for di in d:
    if d[di] > cnt:
        name = di
        cnt = d[di]

print(name)
