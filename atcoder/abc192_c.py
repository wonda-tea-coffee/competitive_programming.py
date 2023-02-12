def f(n):
    l = list(str(n))
    g1 = int("".join(sorted(l, reverse=True)))
    g2 = int("".join(sorted(l)))
    return g1 - g2

N, K = map(int, input().split())
a = N
b = -1
for i in range(1, K+1):
    b = f(a)
    a = b

print(a)