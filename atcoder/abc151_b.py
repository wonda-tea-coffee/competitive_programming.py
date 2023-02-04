N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# (sum(A)+x)/N >= M
# sum(A)+x >= N*M
# x >= N*M - sum(A)
# x = N*M - sum(A)

if N*M - sum(A) <= K:
    print(max(N*M - sum(A), 0))
else:
    print(-1)