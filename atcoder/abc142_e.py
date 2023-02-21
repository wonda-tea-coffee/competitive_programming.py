N, M = map(int, input().split())
cost = []
cap = []
for _ in range(M):
    a, _ = map(int, input().split())
    cost.append(a)

    cap_val = 0
    ci = list(map(lambda x: int(x)-1, input().split()))
    for cij in ci:
        cap_val |= (1<<cij)
    cap.append(cap_val)

INF = float("inf")
dp = [INF]*(1<<N)
dp[0] = 0

for bit in range(1<<N):
    if dp[bit] == INF: continue
    for m in range(M):
        to = bit | cap[m]
        dp[to] = min(dp[to], dp[bit] + cost[m])

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
