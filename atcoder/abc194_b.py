N = int(input())
ans = 10**100
S = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            w = S[i][0] + S[j][1]
        else:
            w = max(S[i][0], S[j][1])

        ans = min(ans, w)

print(ans)
