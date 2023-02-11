N, M = map(int, input().split())
a = []
for _ in range(M):
    input()
    a.append(set(map(int, input().split())))

ans = 0
for n in range(1<<M):
    res = True
    ns = set()
    for i in range(M):
        if (n>>i)&1 == 1:
            ns |= a[i]

    for i in range(1, N+1):
        if not i in ns:
            res = False
            break

    if res:
        ans += 1

print(ans)
