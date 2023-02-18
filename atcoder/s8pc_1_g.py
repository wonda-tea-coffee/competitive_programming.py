def bit_count(n):
    ret = 0
    while n > 0:
        ret += n & 1
        n >>= 1
    return ret

N, M = map(int, input().split())
E = {}
for _ in range(M):
    s, t, d, time = map(int, input().split())
    s, t = s-1, t-1
    E[(s, t)] = (d, time)
    E[(t, s)] = (d, time)

bc = {0: 0}
for i in range(1, 1<<N):
    # スタート地点は訪問済みでないものと扱う
    bc[i] = bit_count(i)-1

INF = float("inf")
goal = []
dp = [[INF]*N for _ in range(1<<N)]
for i in range(N):
    dp[0][i] = 0
    dp[1][i] = 0

for n in range(1<<N):
    # スタートが訪問済みでない
    if n & 1 == 0: continue
    # print("  n =", n)
    for s, t in E:
        if dp[n][s] == INF: continue

        d, time = E[(s, t)]
        # 頂点sが訪問済みでない
        if (n>>s)&1 == 0: continue
        # 頂点tに既に訪問している
        if (n>>t)&1 == 1: continue
        # 道路が閉鎖されている
        if bc[n] > time: continue

        m = n | (1<<t)
        # print("    m =", m, "s =", s, " t =", t, ", d =", d)
        # print("    ", dp[m][t], dp[n][s] + d)
        dp[m][t] = min(dp[m][t], dp[n][s] + d)

# print(dp[-1])
for i in range(N):
    # print("  i =", i, "dp[-1][i] =", dp[-1][i], (i, start) in E)
    if dp[-1][i] == INF: continue
    if not (i, 0) in E: continue
    d, time = E[(i, 0)]
    # print("    d, time = ", d, time)
    if N > time: continue
    goal.append(dp[-1][i] + d)

cnt = 0
minpath = INF
for x in goal:
    if x < minpath:
        cnt = 1
        minpath = x
    elif x == minpath:
        cnt += 1

if minpath == INF:
    print("IMPOSSIBLE")
else:
    print(minpath, cnt)
