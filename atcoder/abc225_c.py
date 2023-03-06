N, M = map(int, input().split())
ll = []
for n in range(N):
    l = []
    B = list(map(int, input().split()))
    for m in range(M):
        j = B[m] % 7
        if j == 0: j = 7
        i = (B[m] - j)//7 + 1
        l.append((i, j))
    ll.append(l)

sr = ll[0][0][0]
sc = ll[0][0][1]

for n in range(N):
    for m in range(M):
        if (sr+n, sc+m) == ll[n][m]:
            pass
        else:
            print("No")
            exit()

print("Yes")
