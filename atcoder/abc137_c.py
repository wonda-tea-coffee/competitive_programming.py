from collections import defaultdict

N = int(input())
a = defaultdict(int)
for _ in range(N):
    si = input()
    d = defaultdict(int)
    for sij in si:
        d[sij] += 1
    res = []
    for w in sorted(d.keys()):
        res.append(w*d[w])
    a["".join(res)] += 1

ans = 0
for ai in a:
    ans += a[ai]*(a[ai]-1)//2
print(ans)
