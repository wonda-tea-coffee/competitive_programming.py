# N-1個の区間から最小のものをN-M個選ぶ

N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

if N >= M:
    print(0)
    exit()

dist = []
for i in range(1, M):
    dist.append(abs(X[i]-X[i-1]))
dist.sort()

ans = 0

for i in range(M-N):
    ans += dist[i]
print(ans)
