N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        c = 0
        for k in range(M):
            if S[i][k] == "o" or S[j][k] == "o":
                c += 1
        if c == M:
            ans += 1
print(ans)