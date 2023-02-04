from itertools import combinations

N = int(input())
L = set([tuple(map(int, input().split())) for _ in range(N)])

ans = 0
for p1, p2 in combinations(L, 2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    p3 = (p1[0] + dy, p1[1] - dx)
    p4 = (p2[0] + dy, p2[1] - dx)
    if p3 in L and p4 in L:
        ans = max(ans, dx*dx + dy*dy)

print(ans)
