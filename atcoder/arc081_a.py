from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for ai in A:
    d[ai] += 1
Q = []
for di in d:
    Q.append((-di, d[di]))
Q.sort()

ans = []
for num, cnt in Q:
    c = cnt
    while c >= 2:
        c -= 2
        ans.append(-num)
    if len(ans) >= 2: break

if len(ans) < 2:
    print(0)
else:
    print(ans[0] * ans[1])
