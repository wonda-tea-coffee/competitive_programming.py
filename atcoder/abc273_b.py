X, K = map(int, input().split())

for i in range(1, K+1):
    d = 10**i
    y = X % d
    X -= y
    # print(y, X)
    if y // (d//10) >= 5:
        X += d
    # print(i, X)
print(X)