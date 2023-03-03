from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for i in range(1, M+1):
    p, y = map(int, input().split())
    d[p].append((y, i))
ans = [0]*(M+1)

for di in d:
    d[di].sort()
    for rank, (_, idx) in enumerate(d[di], 1):
        ans[idx] = "%06d%06d" % (di, rank)

for a in ans[1:]:
    print(a)
