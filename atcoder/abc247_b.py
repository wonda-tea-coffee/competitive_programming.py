import sys

N = int(input())
st = [tuple(input().split()) for _ in range(N)]

for i in range(N):
    fs = True
    ft = True
    for j in range(N):
        if i == j: continue
        fs &= st[i][0] != st[j][0] and st[i][0] != st[j][1]
        ft &= st[i][1] != st[j][0] and st[i][1] != st[j][1]

    if not fs and not ft:
        print("No")
        sys.exit(0)

print("Yes")
