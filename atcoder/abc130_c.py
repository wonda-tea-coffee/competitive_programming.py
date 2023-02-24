W, H, x, y = map(int, input().split())

ans1 = W*H/2
ans2 = 0
if x*2 == W and y*2 == H:
    ans2 = 1
print(ans1, ans2)
