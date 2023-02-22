N, K = map(int, input().split())

s = 0
for i in range(1, min(K, N+1)):
    t = 0
    j = i
    while j < K:
        t += 1
        j *= 2
    s += 1/(N*2**t)

if K <= N:
    ans = 1 + s - (K-1)/N
else:
    ans = s
print(ans)
