N = int(input())
A = list(map(int, input().split()))
P = 0
M = 4
B = [False] * M

for i in range(N):
    B[0] = True
    for j in range(M-1, -1, -1):
        if not B[j]: continue

        if j + A[i] >= M:
            B[j] = False
            P += 1
        else:
            B[j] = False
            B[j + A[i]] = True
    # print(B)

print(P)