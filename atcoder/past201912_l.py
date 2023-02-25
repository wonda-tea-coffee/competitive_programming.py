import heapq
from collections import deque

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(.5)

N, M = map(int, input().split())
# 大きい塔
X = []
Y = []
C = []
for _ in range(N):
    xi, yi, ci = map(int, input().split())
    X.append(xi)
    Y.append(yi)
    C.append(ci)
# 小さい塔
x = []
y = []
c = []
for _ in range(M):
    xi, yi, ci = map(int, input().split())
    x.append(xi)
    y.append(yi)
    c.append(ci)

ALL = 1 << M

# 小さい塔の含め方でそれぞれ最小全域木を求める
ans = 10**100
for bit in range(ALL):
    Q = []

    # 大きい塔0から他の大きい塔
    for i in range(1, N):
        cost = dist(X[0], Y[0], X[i], Y[i])
        if C[0] != C[i]: cost *= 10
        heapq.heappush(Q, (cost, i))

    # 大きい塔0から小さい塔
    sc = 0
    edges = list(range(N))
    for m in range(M):
        if (bit>>m)&1 == 0: continue
        sc += 1
        cost = dist(X[0], Y[0], x[m], y[m])
        if C[0] != c[m]: cost *= 10
        # 小さい塔の頂点番号はオフセット+Nで管理
        heapq.heappush(Q, (cost, m+N))
        edges.append(m+N)

    cost_sum = 0
    marked_count = 1
    marked_big = [False]*N
    marked_sml = [False]*M
    marked_big[0] = True

    while marked_count < N+sc:
        cost, cur = heapq.heappop(Q)

        if cur < N:
            if marked_big[cur]: continue
            marked_big[cur] = True
        else:
            if marked_sml[cur-N]: continue
            marked_sml[cur-N] = True

        marked_count += 1
        cost_sum += cost

        if cur < N:
            ix, iy, ic = X[cur], Y[cur], C[cur]
        else:
            ix, iy, ic = x[cur-N], y[cur-N], c[cur-N]
        for to in edges:
            if to < N:
                if marked_big[to]: continue
                jx, jy, jc = X[to], Y[to], C[to]
            else:
                if marked_sml[to-N]: continue
                jx, jy, jc = x[to-N], y[to-N], c[to-N]

            ncost = dist(ix, iy, jx, jy)
            if ic != jc: ncost *= 10
            heapq.heappush(Q, (ncost, to))

    ans = min(ans, cost_sum)

print(ans)
