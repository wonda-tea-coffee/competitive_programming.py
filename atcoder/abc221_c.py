N = list(map(int, list(input())))
M = len(N)

ans = 0
for bit in range(1, 1<<M-1):
    a = []
    b = []
    for i in range(M):
        if (bit>>i)&1:
            a.append(N[i])
        else:
            b.append(N[i])

    an = int("".join(sorted(map(str, a), reverse=True)))
    bn = int("".join(sorted(map(str, b), reverse=True)))
    # print(an, bn)
    ans = max(ans, an*bn)

print(ans)
