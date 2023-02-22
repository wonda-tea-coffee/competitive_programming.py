from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
for a in A:
    d[a] += 1

Q = []
for di in d:
    Q.append((d[di], di))
Q.sort()

if len(Q) <= K:
    print(0)
    exit()

ans = 0
s = len(Q)
i = 0
while s > K:
    ans += Q[i][0]
    s -= 1
    i += 1
print(ans)
