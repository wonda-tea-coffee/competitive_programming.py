N, K = map(int, input().split())
A = list(map(int, input().split()))
M = 3*10**5 + 1
check = [False]*M
for i in range(N):
    if A[i] >= M: continue
    check[A[i]] = True

ans = 0
while check[ans] and ans < K:
    ans += 1
print(ans)
