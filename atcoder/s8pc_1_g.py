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
    # jからkに向かうとする
    for j, k in E:
        # この状態に来ることができない
        if num_dp[bit][j] == 0: continue
        # kが既に訪問済み
        if (bit>>k)&1 == 1: continue

        d, time = E[(j, k)]
        ndist = dist_dp[bit][j] + d
        # 道が既に封鎖されている
        if ndist > time: continue

        to = bit | (1<<k)
        if dist_dp[to][k] == ndist:
            num_dp[to][k] += num_dp[bit][j]
        elif dist_dp[to][k] > ndist:
            num_dp[to][k] = num_dp[bit][j]
        dist_dp[to][k] = min(dist_dp[to][k], ndist)

if dist_dp[-1][0] == INF:
    print("IMPOSSIBLE")
else:
    print(dist_dp[-1][0], num_dp[-1][0])
