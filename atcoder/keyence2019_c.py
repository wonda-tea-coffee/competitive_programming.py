N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for a, b in zip(A, B):
    C.append(a-b)
C.sort()

r = N-1
D = list(C)
for i in range(N):
    if D[i] >= 0: continue
    while D[i] < 0:
        if D[r] <= 0:
            print(-1)
            exit()
        elif -D[i] <= D[r]:
            D[r] += D[i]
            D[i] = 0
        else:
            D[i] += D[r]
            D[r] = 0
            r -= 1

ans = 0
for i in range(N):
    if C[i] != D[i]: ans += 1
print(ans)
