from collections import defaultdict
from itertools import combinations

N = int(input())
d = defaultdict(int)
for _ in range(N):
    d[input()[0]] += 1

ans = 0
for c1, c2, c3 in combinations(["M", "A", "R", "C", "H"], 3):
    ans += d[c1]*d[c2]*d[c3]

print(ans)
