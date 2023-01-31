T, N = map(int, input().split())

max_score = [0]*(N+1)

for i in range(T):
    p = list(map(int, input().split()))
    ans = 0
    for j in range(N):
        max_score[j] = max(max_score[j], p[j])
        ans += max_score[j]
    print(ans)
