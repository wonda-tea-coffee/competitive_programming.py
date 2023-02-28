import sys
input = lambda: sys.stdin.readline().rstrip()

def show_grid(v, rotate, f1, f2):
    ans = [[False]*(N+1) for _ in range(N+1)]

    for x, y, r, g1, g2 in v:
        nx = x
        ny = y
        while r != rotate:
            nx, ny = ny, N-nx+1
            r = (r+1)%4
        if f1 != g1:
            nx = N-nx+1
        if f2 != g2:
            ny = N-ny+1
        ans[nx][ny] = not ans[nx][ny]

    for i in range(1, N+1):
        row = []
        for j in range(1, N+1):
            if ans[i][j]:
                row.append("1")
            else:
                row.append("0")
        print("".join(row))
    print()

N, Q = map(int, input().split())
v = []
rotate = 0
f1 = False
f2 = False
for _ in range(Q):
    t, *q = input().split()

    if t == "1":
        x, y = map(int, q)
        v.append((x, y, rotate, f1, f2))
    elif t == "2":
        c = q[0]
        if c == "A":
            rotate += 1
        else:
            rotate -= 1
        rotate %= 4
    else:
        c = q[0]
        if c == "A":
            f1 = not f1
        else:
            f2 = not f2

show_grid(v, rotate, f1, f2)
