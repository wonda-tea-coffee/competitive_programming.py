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
    E[(s-1, t-1)] = (d, time)
    E[(t-1, s-1)] = (d, time)

bc = {0: 0}
for i in range(1, 1<<N):
    # スタート地点は訪問済みでないものと扱う
    bc[i] = bit_count(i)-1

INF = float("inf")
goal = []
dp = [[INF]*N for _ in range(1<<N)]
for i in range(N):
    dp[0][i] = (0, 0)
    dp[1][i] = (0, 0)

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
        ndp = dp[n][s][0] + d
        if dp[m][t] == INF or ndp < dp[m][t][0]:
            dp[m][t] = (ndp, dp[n][s][1])
        elif ndp == dp[m][t][0]:
            dp[m][t][1] += 1

# print(dp[-1])
for i in range(N):
    # print("  i =", i, "dp[-1][i] =", dp[-1][i], (i, start) in E)
    if dp[-1][i] == INF: continue
    if not (i, 0) in E: continue
    d, time = E[(i, 0)]
    # print("    d, time = ", d, time)
    if N-1 > time: continue
    print(i, dp[-1][i][0], d)

# cnt = 0
# minpath = INF
print(goal)
