T, N = map(int, input().split())
cmax = [0]*N
for _ in range(T):
    P = list(map(int, input().split()))
    for i in range(N):
        cmax[i] = max(cmax[i], P[i])
    print(sum(cmax))
