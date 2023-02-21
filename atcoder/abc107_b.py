H, W = map(int, input().split())
a = [input() for _ in range(H)]
r = [True]*H
c = [True]*W

for i in range(H):
    r[i] = set(a[i]) == {"."}
for wi in range(W):
    for hi in range(H):
        c[wi] &= a[hi][wi] == "."

for i in range(H):
    if r[i]: continue
    for j in range(W):
        if c[j]: continue
        print(a[i][j], end="")
    print()
