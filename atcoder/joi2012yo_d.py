N, K = map(int, input().split())
MOD = 10_000
F = [-1]*N
for _ in range(K):
    a, b = map(lambda x: int(x)-1, input().split())
    F[a] = b
dp = [[[0]*3 for _ in range(3)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    if F[i] == -1:
        cs = [0, 1, 2]
    else:
        cs = [F[i]]
    for a in range(3):
        for b in range(3):
            for c in cs:
                if i >= 2 and a == b == c: continue
                dp[i+1][b][c] += dp[i][a][b]
                dp[i+1][b][c] %= MOD

ans = 0
for a in range(3):
    for b in range(3):
        ans += dp[N][a][b]
        ans %= MOD
print(ans)
