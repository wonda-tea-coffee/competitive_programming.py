import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = [tuple(map(lambda x: int(x)*2, input().split())) for _ in range(N)]
T = [tuple(map(lambda x: int(x)*2, input().split())) for _ in range(N)]

if set(S) == set(T):
    print("Yes")
    exit()

# x軸に平行な直線に関する対称移動を試す
def check1():
    y = [S[0]]
    for s in S[1:]:
        if s[1] == S[0][1]:
            y.append(s)
    Y = []
    for t in T:
        if t[1] == S[0][1]:
            Y.append(t)

    if len(y) != len(Y): return False

    y.sort()
    Y.sort()

    x = (y[0][0]+Y[-1][0])//2
    U = []
    for tx, ty in T:
        d = abs(x-tx)
        if tx <= x:
            ux = tx + 2*d
        else:
            ux = tx - 2*d
        U.append((ux, ty))

    return set(S) == set(U)

# y軸に平行な直線に関する対称移動を試す
def check2():
    x = [S[0]]
    for s in S[1:]:
        if s[0] == S[0][0]:
            x.append(s)
    X = []
    for t in T:
        if t[0] == S[0][0]:
            X.append(t)

    if len(x) != len(X): return False

    x.sort()
    X.sort()

    y = (x[0][1]+X[-1][1])//2
    U = []
    for tx, ty in T:
        d = abs(y-ty)
        if ty <= y:
            uy = ty + 2*d
        else:
            uy = ty - 2*d
        U.append((tx, uy))

    return set(S) == set(U)

if check1() or check2():
    print("Yes")
else:
    print("No")
