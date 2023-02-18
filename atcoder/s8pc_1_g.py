N, M = map(int, input().split())
dist = [[-1]*N for _ in range(N)]
time = [[-1]*N for _ in range(N)]
for _ in range(M):
    s, t, d, time1 = map(int, input().split())
    s, t = s-1, t-1
    dist[s][t] = dist[t][s] = d
    time[s][t] = time[t][s] = time1
INF = float("inf")
dist_dp = [[INF]*N for _ in range(1<<N)]
num_dp  = [[0]*N for _ in range(1<<N)]
dist_dp[0][0] = 0
num_dp[0][0] = 1

for bit in range(1<<N):
    for j in range(N):
        if num_dp[bit][j] == 0: continue
        for k in range(N):
            if (bit>>k)&1 == 1: continue
            if dist[j][k] == -1: continue

            ndist = dist_dp[bit][j] + dist[j][k]
            if ndist > time[j][k]: continue

            to = bit | (1<<k)
            if dist_dp[to][k] > ndist:
                dist_dp[to][k] = ndist
                num_dp[to][k] = num_dp[bit][j]
            elif dist_dp[to][k] == ndist:
                num_dp[to][k] += num_dp[bit][j]

if dist_dp[-1][0] == INF:
    print("IMPOSSIBLE")
else:
    print(dist_dp[-1][0], num_dp[-1][0])
