H, W, N = map(int, input().split())
row = []
col = []
for i in range(N):
    A, B = map(int, input().split())
    row.append((A, i))
    col.append((B, i))

row.sort()
col.sort()

ansrow = [-1]*(N+1)
anscol = [-1]*(N+1)
idxrow = 1
idxcol = 1
for i in range(N):
    if i > 0 and row[i][0] != row[i-1][0]:
        idxrow += 1
    if i > 0 and col[i][0] != col[i-1][0]:
        idxcol += 1

    ansrow[row[i][1]] = idxrow
    anscol[col[i][1]] = idxcol

for i in range(N):
    print(ansrow[i], anscol[i])