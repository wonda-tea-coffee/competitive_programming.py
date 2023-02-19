from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]
d = defaultdict(lambda: 0)
for si in S:
    d[si] += 1
maxcnt = 0
ans = []
for w in d:
    if d[w] > maxcnt:
        maxcnt = d[w]
        ans = [w]
    elif d[w] == maxcnt:
        ans.append(w)

print("\n".join(sorted(ans)))
