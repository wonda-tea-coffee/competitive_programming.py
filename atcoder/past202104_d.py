N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * N
S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]

for x in range(N-K+1):
    #   A[x] + A[x+1] + ... + A[x+K-1]
    # = (A[0] + A[1] + ... + A[N-1]) - (A[0] + A[1] + ... + A[x-1]) - (A[x+K] + A[x+K+1] + ... + A[N-1])
    ans = S[N-1]
    if x != 0: ans -= S[x-1]
    ans -= S[N-1] - S[x+K-1]
    print(ans)
