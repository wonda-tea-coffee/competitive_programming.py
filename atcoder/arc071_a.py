import string
from collections import defaultdict

n = int(input())
S = [input() for _ in range(n)]
cnt = [defaultdict(int) for _ in range(n)]
for i in range(n):
    for sij in S[i]:
        cnt[i][sij] += 1

ans = ""
for c in string.ascii_lowercase:
    mincnt = 100
    for i in range(n):
        mincnt = min(mincnt, cnt[i][c])
    ans += c*mincnt
print(ans)
