H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))
T = []
for _ in range(H):
    T.append(list(input()))

def shrink(t):
    miny = H
    maxy = 0
    minx = W
    maxx = 0
    for i in range(H):
        for j in range(W):
            if t[i][j] == "#":
                miny = min(miny, i)
                maxy = max(maxy, i)
                minx = min(minx, j)
                maxx = max(maxx, j)

    ret = [[None]*(maxx-minx+1) for _ in range(maxy-miny+1)]
    for i in range(maxy+1):
        for j in range(maxx+1):
            ret[i][j] = t[i+miny][j+minx]
    return ret

def rotate(t):
    h = len(t)
    w = len(t[0])
    ret = [[None]*h for _ in range(w)]

    for i in range(w):
        for j in range(h):
            ret[i][j] = t[j][w-i-1]

    return ret

def search(t):
    pass

def stamp(t):
    pass

T = shrink(T)
for _ in range(3):
    if search(T):
        exit(print("Yes"))
    T = rotate(T)

print("No")
