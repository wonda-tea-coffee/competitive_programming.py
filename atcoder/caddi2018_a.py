N, P = map(int, input().split())

if N == 1:
    exit(print(P))

m = 0
d = 2
a = []
q = P
while d*d <= P:
    c = 0
    while q % d == 0:
        q //= d
        c += 1
    if c > 0: a.append((d, c))
    d += 1

ans = 1
# print(a)
for di, c in a:
    ans *= di ** (c//N)
print(ans)
