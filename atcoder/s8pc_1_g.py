# オリジナル
# https://atcoder.jp/contests/s8pc-1/submissions/38738519

N, M = map(int, input().split())
INF = float("inf")
dist = [[INF]*N for i in range(N)]
time = [[0]*N for i in range(N)]
for i in range(M):
    s, t, d, time_1 = map(int, input().split())
    s, t = s-1, t-1
    dist[s][t] = d
    time[s][t] = time_1
    dist[t][s] = d
    time[t][s] = time_1

# dp[通ったとこ][今いるとこ]->今まで通ったところから今に至るまでの最短経路の距離,通り数
# dp[S+k][k]=dp[S][j]+cost(j,k)
# ans -> dp[1<<N][0] ∵0から始めても一般性を失わず，最後は0に帰ってくるから．
dist_dp = [[INF]*N for i in range(1<<N)]
num_dp = [[0]*N for i in range(1<<N)]

dist_dp[0][0] = 0
num_dp[0][0] = 1

for bit in range(1<<N):
    # jからkに向かうとする
    for j in range(N):
        # この状態に来ることができない
        if num_dp[bit][j] == 0: continue

        for k in range(N):
            # kが既に訪問済み
            if (bit>>k) & 1 == 1: continue
            # 道路が無い
            if dist[j][k] == INF: continue
            ndist = dist_dp[bit][j] + dist[j][k]
            # 道が既に封鎖されている
            if ndist > time[j][k]: continue

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
