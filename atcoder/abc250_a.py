H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    if 1 <= R+y <= H and 1 <= C+x <= W:
        ans += 1

print(ans)
