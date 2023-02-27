N, K = map(int, input().split())
A = list(map(int, input().split()))
M1 = N//2
M2 = N-M1
A1 = A[:M1]
A2 = A[M1:]

memo = set()
for bit in range(1<<M1):
    c = 0
    for i in range(M1):
        if (bit>>i)&1 == 1:
            c += A1[i]
    memo.add(c)

for bit in range(1<<M2):
    c = 0
    for i in range(M2):
        if (bit>>i)&1 == 1:
            c += A2[i]
    if K-c in memo:
        print("Yes")
        exit()

print("No")
