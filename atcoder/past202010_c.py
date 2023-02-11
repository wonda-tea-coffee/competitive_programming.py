import itertools

N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

T = []
for i in range(N):
    l = ""
    for j in range(M):
        c = 0
        for dy, dx in itertools.product([-1, 0, 1], repeat=2):
            ni = i + dy
            nj = j + dx
            if 0 <= ni < N and 0 <= nj < M and S[ni][nj] == "#":
                c += 1
        l += str(c)
    T.append(l)

for i in range(N):
    print(T[i])
