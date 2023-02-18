V, E = map(int, input().split())
G = {}
for _ in range(E):
    s, t, d = map(int, input().split())
    G[(s, t)] = d
INF = float("inf")
dp = [[INF]*V for _ in range(1<<V)]
dp[0][0] = 0

for bit in range(1<<V):
    for s, t in G:
        if dp[bit][s] == INF: continue
        if bit != 0 and (bit>>s)&1 == 0: continue
        if (bit>>t)&1 == 1: continue
        to = bit | (1<<t)
        dp[to][t] = min(dp[to][t], dp[bit][s] + G[(s, t)])

if dp[-1][0] == INF:
    print(-1)
else:
    print(dp[-1][0])
