N = int(input())
A = list(map(int, input().split()))
ans = 10**100

for ai in A:
    s = 0
    t = ai
    while t % 2 == 0:
        t //= 2
        s += 1

    ans = min(ans, s)

print(ans)