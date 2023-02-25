N = int(input())
S = " " + input()
C = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))
INF = 10**100
cost = [[INF]*(N+1) for _ in range(N+1)]
cost[0][0] = 0

for i in range(1, N):
    for j in range(i):
        if S[i] == "(":
            # そのまま使う
            cost[i][j+1] = min(cost[i][j+1], cost[i-1][j])
            # 反転する
            if j > 0:
                cost[i][j-1] = min(cost[i][j-1], cost[i-1][j] + C[i])
        else:
            # そのまま使う
            if j > 0:
                cost[i][j-1] = min(cost[i][j-1], cost[i-1][j])
            # 反転する
            cost[i][j+1] = min(cost[i][j+1], cost[i-1][j] + C[i])
        # 削除する
        cost[i][j] = min(cost[i][j], cost[i-1][j] + D[i])

print(cost[N][0])
