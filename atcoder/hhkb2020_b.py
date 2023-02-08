H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
ans = 0

for i in range(H):
    for j in range(W-1):
        if S[i][j] == S[i][j+1] == ".":
            ans += 1
for i in range(H-1):
    for j in range(W):
        if S[i][j] == S[i+1][j] == ".":
            ans += 1

print(ans)