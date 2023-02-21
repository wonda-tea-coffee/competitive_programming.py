N, M = map(int, input().split())
S = []
C = []
for _ in range(M):
    s, c = input().split()
    S.append(s)
    C.append(int(c))
INF = float("inf")
dp = [INF]*(1<<N)
dp[0] = 0

for bit in range(1<<N):
    if dp[bit] == INF: continue
    for m in range(M):
        to = bit
        for si in range(N):
            if S[m][si] == "N": continue
            to |= 1<<si
        dp[to] = min(dp[to], dp[bit] + C[m])

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
