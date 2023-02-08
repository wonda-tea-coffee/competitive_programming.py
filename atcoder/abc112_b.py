N, T = map(int, input().split())
ans = "TLE"

for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        if ans == "TLE":
            ans = c
        else:
            ans = min(ans, c)

print(ans)
