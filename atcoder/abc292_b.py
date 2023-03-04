N, Q = map(int, input().split())
yellow = [0]*(N+1)
red = [0]*(N+1)
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        yellow[x] += 1
    elif t == 2:
        red[x] += 1
    else:
        if yellow[x] >= 2 or red[x] > 0:
            print("Yes")
        else:
            print("No")
