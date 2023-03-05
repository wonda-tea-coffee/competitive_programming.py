from itertools import combinations

# 3点が一直線上に並んでいるか
def is_alignment(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1]) == 0

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b, c in combinations(P, 3):
    if is_alignment(a, b, c): continue
    ans += 1

print(ans)
