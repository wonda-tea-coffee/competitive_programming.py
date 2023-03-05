def check(sp, tp):
    s = set()
    for i in range(len(sp)):
        ys, xs = sp[i]
        yt, xt = tp[i]
        s.add((ys-yt, xs-xt))

    return len(s) == 1

def rotate(sp):
    ret = []

    for y, x in sp:
        ret.append((x, N-y-1))

    return ret

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]
sp = []
tp = []
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            sp.append((i, j))
        if T[i][j] == "#":
            tp.append((i, j))
tp.sort()

if len(sp) != len(tp):
    print("No")
    exit()

def debug(sp):
    print()
    for i in range(N):
        for j in range(N):
            if (i, j) in sp:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

for i in range(4):
    # debug(sp)
    if check(sorted(sp), tp):
        print("Yes")
        exit()
    sp = rotate(sp)

print("No")
