N, K = map(int, input().split())
h = sorted([int(input()) for _ in range(N)])
ans = 10**10

# i+K-1 < N
# i < N-K+1

for i in range(N-K+1):
    ans = min(ans, h[i+K-1] - h[i])

print(ans)
