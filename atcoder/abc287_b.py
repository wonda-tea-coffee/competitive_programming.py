N, M = map(int, input().split())
S, T = [], []

for _ in range(N):
    S.append(int(input()) % 1000)
for _ in range(M):
    T.append(int(input()))

ans = 0
for si in S:
    for ti in T:
        if si == ti:
            ans += 1
            break

print(ans)
