N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)

m = N//2-1
for i in range(N):
    if X[i] > Y[m]:
        print(Y[m])
    else:
        print(Y[m+1])
