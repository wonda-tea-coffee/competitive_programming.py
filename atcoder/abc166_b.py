N, K = map(int, input().split())
X = set(range(1, N+1))
for _ in range(K):
    input()
    X -= set(map(int, input().split()))

print(len(X))