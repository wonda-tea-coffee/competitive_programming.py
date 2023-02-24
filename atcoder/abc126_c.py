N, K = map(int, input().split())
ans = 0

for i in range(1, N+1):
    t = 1
    j = i
    while j < K:
        j *= 2
        t /= 2
    # print(i, t)
    ans += t/N

print(ans)
