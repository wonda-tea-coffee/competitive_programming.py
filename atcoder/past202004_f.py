N = int(input())
cnt = [0]*101
X = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    X[a-1].append(b)

ans = 0
for d in range(N):
    for xd in X[d]:
        cnt[xd] += 1

    for i in range(100, -1, -1):
        if cnt[i] == 0: continue
        cnt[i] -= 1
        ans += i
        break

    print(ans)
