R, C = map(int, input().split())
G = []
for _ in range(R):
    G.append(list(map(int, input().split())))

ans = 0
for ri in range(1<<R):
    s = 0
    for ci in range(C):
        t = 0
        for ri2 in range(R):
            if (ri>>ri2)&1 == G[ri2][ci]:
                t += 1

        s += max(R-t, t)

    ans = max(ans, s)

print(ans)
