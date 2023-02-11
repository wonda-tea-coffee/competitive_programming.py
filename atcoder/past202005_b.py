from collections import defaultdict

N, M, Q = map(int, input().split())
q = [0] * (M+1)
S = [[] for _ in range(N+1)]
res = []
for _ in range(Q):
    s, *t = map(int, input().split())

    if s == 1:
        n = t[0]
        ans = 0
        for si in S[n]:
            ans += N - q[si]
        res.append(ans)
    else:
        n, m = t
        S[n].append(m)
        q[m] += 1

for r in res:
    print(r)