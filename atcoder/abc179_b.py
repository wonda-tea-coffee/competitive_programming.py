N = int(input())
ans = 0
cnt = 0
for _ in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
if ans >= 3:
    print("Yes")
else:
    print("No")