N, M, X, T, D = map(int, input().split())
# Y + X*D = T
# Y = T - X*D

print(T - X*D + min(X, M)*D)