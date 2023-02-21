import bisect

N = int(input())
X = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    X[a-1].append(b)
cnt = [0]*101
ans = 0

for d in range(N):
    for x in X[d]:
        cnt[x] += 1

    for i in range(100, -1, -1):
        if cnt[i] == 0: continue
        ans += i
        cnt[i] -= 1
        break

    print(ans)
