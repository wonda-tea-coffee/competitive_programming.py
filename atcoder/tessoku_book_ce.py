N = int(input())
A = list(map(int, input().split()))
atarisum = [0]
for ai in A:
    d = atarisum[-1]
    if ai == 1: d += 1
    atarisum.append(d)
Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())
    atari = atarisum[R] - atarisum[L-1]
    hazure = R-L+1-atari
    if atari > hazure:
        print("win")
    elif atari < hazure:
        print("lose")
    else:
        print("draw")
