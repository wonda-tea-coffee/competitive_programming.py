N, M, K = map(int, input().split())
memo = set()
for a in range(M+1):
    for b in range(N+1):
        memo.add(a*N + b*M - 2*a*b)

if K in memo:
    print("Yes")
else:
    print("No")
