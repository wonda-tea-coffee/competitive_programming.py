K, N = map(int, input().split())
A = list(map(int, input().split()))
d = [(A[0] - A[-1]) % K]
for i in range(N-1):
    d.append(A[i+1] - A[i])

print(sum(d) - max(d))
