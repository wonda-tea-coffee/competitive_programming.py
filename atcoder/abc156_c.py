N = int(input())
X = list(map(int, input().split()))
ans = 10**100
for p in range(1, 101):
    c = 0
    for xi in X:
        c += abs(xi - p)**2

    ans = min(ans, c)

print(ans)