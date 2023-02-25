N, K, S = map(int, input().split())
L = 10**9
if S == L:
    L -= 1
ans = [S]*K + [L]*(N-K)
print(*ans)
