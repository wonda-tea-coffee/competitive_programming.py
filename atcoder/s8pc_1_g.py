# オリジナル
# https://atcoder.jp/contests/s8pc-1/submissions/38738519

N, M = map(int, input().split())
E = {}
for _ in range(M):
    s, t, d, time = map(int, input().split())
    s, t = s-1, t-1
    E[(s, t)] = (d, time)
    E[(t, s)] = (d, time)
INF = float("inf")
dist_dp = [[INF]*N for i in range(1<<N)]
num_dp = [[0]*N for i in range(1<<N)]
dist_dp[0][0] = 0
num_dp[0][0] = 1

for bit in range(1<<N):
    for s, t in E:
        if num_dp[bit][s] == 0: continue
        if (bit>>t)&1 == 1: continue

        d, time = E[(s, t)]
        nd = dist_dp[bit][s] + d
        if nd > time: continue

        to = bit | (1<<t)
        if dist_dp[to][t] > nd:
            num_dp[to][t] = num_dp[bit][s]
        elif dist_dp[to][t] == nd:
            num_dp[to][t] += num_dp[bit][s]
        dist_dp[to][t] = min(dist_dp[to][t], nd)

if dist_dp[-1][0] == INF:
    print("IMPOSSIBLE")
else:
    print(dist_dp[-1][0], num_dp[-1][0])
