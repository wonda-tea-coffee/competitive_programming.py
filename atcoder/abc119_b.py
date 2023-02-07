N = int(input())
ans = 0
for _ in range(N):
    x, y = input().split()
    x = float(x)
    if y == "JPY":
        ans += x
    else:
        ans += x * 380000

print(ans)