G, W, H = map(int, input().split())
s = (0, "S")
g = (G, "G")
w = (W, "W")
h = (H, "H")
m = sorted([s, g, w, h])

si = m.index(s)
gi = m.index(g)

if abs(si - gi) == 1:
    print(abs(G))
elif abs(si - gi) == 2:
    # S * G *
    if si == 0:
        if m[si+1] == h:
            print(abs(G))
        else:
            print(-1)
    # * S * G
    elif si == 1:
        if m[si+1] == h:
            print(abs(G))
        else:
            print(2*abs(H) + abs(G))
    # G * S *
    elif si == 2:
        if m[si-1] == h:
            print(abs(G))
        else:
            print(2*abs(H) + abs(G))
    # * G * S
    else:
        if m[si-1] == h:
            print(abs(G))
        else:
            print(-1)
else:
    # S * * G
    # G * * S
    if (si == 0 and m[si+1] == h and m[si+2] == w) or(si == 3 and m[si-1] == h and m[si-2] == w):
        print(abs(G))
    else:
        print(-1)