H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

for wi in range(W):
    for hi in range(H):
        print(A[hi][wi], end=" ")
    print()
