import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = [tuple(map(lambda x: int(x)*2, input().split())) for _ in range(N)]
T = [tuple(map(lambda x: int(x)*2, input().split())) for _ in range(N)]

def check1():
    p = []
    for sx, sy in S:
        if sy == S[0][1]:
            p.append((sx, sy))
    q = []
    for tx, ty in T:
        if ty == S[0][1]:
            q.append((tx, ty))

    # print(p, q)
    if len(p) != len(q): return False

    p.sort()
    q.sort()
    x = (p[0][0]+q[-1][0])//2
    U = []
    for tx, ty in T:
        d = abs(tx - x)
        if tx < x:
            ntx = tx + 2*d
        else:
            ntx = tx - 2*d
        U.append((ntx, ty))

    return set(S) == set(U)

def check2():
    p = []
    for sx, sy in S:
        if sx == S[0][0]:
            p.append((sx, sy))
    q = []
    for tx, ty in T:
        if tx == S[0][0]:
            q.append((tx, ty))

    # print(p, q)
    if len(p) != len(q): return False

    p.sort()
    q.sort()
    y = (p[0][1]+q[-1][1])//2
    U = []
    for tx, ty in T:
        d = abs(ty - y)
        if ty < y:
            nty = ty + 2*d
        else:
            nty = ty - 2*d
        U.append((tx, nty))

    return set(S) == set(U)

if set(S) == set(T):
    print("Yes")
    exit()

if check1() or check2():
    print("Yes")
else:
    print("No")
