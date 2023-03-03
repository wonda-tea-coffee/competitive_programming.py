N, K = map(int, input().split())
P = list(map(int, input().split()))
T = [-1] + list(map(lambda x: {"r":0, "s":1, "p":2}[x], list(input())))
memo = [-1]*(N+1)
ans = 0
for i in range(1, N+1):
    win = (T[i]+2) % 3
    if i < K:
        memo[i] = win
        ans += P[win]
    elif win == memo[i-K]:
        if i+K <= N:
            te = [{0,1,2}-{win, (T[i+K]+2)%3}][0]
            memo[i] = te
    else:
        memo[i] = win
        ans += P[win]

print(ans)
