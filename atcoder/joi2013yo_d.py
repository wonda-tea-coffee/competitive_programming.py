D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
A = []
B = []
C = []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
# dp[i][j] := i日目までで、最後に服jを選んだ場合の最大値
dp = [[0]*N for _ in range(D)]
for i in range(N):
    if A[i] <= T[0] <= B[i]:
        pass
    else:
        dp[0][i] = -10000

for i in range(1, D):
    # i日目に着られる服の候補
    cs = []
    for j in range(N):
        if A[j] <= T[i] <= B[j]:
            cs.append(j)
    for csi in cs:
        for j in range(N):
            dp[i][csi] = max(dp[i][csi], dp[i-1][j] + abs(C[j] - C[csi]))
    # print("i=", i, "cs=", cs, "dp=", dp)

print(max(dp[-1]))
