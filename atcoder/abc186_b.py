H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

m = 10**100
s = 0
for i in range(H):
    m = min(m, *A[i])
    s += sum(A[i])

# print(s, m)
print(s - m*H*W)
