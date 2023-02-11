N, K = map(int, input().split())
c = list(map(int, input().split()))
p = list(map(int, input().split()))

A = []
for i in range(N):
    A.append((p[i], c[i]))
A.sort()

buy = set()
ans = 0
for pi, ci in A:
    if ci in buy: continue
    buy.add(ci)
    ans += pi
    if len(buy) == K:
        print(ans)
        exit()

print(-1)
