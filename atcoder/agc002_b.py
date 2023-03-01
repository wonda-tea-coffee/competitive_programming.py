N, M = map(int, input().split())
ball = [1]*(N+1)
flag = [False]*(N+1)
red = 1
flag[red] = True

for _ in range(M):
    x, y = map(int, input().split())
    ball[x] -= 1
    ball[y] += 1
    if flag[x]:
        flag[y] = True
    if ball[x] == 0:
        flag[x] = False

# print(*flag[1:])
# print(*ball[1:])

ans = 0
for i in range(1, N+1):
    if flag[i] and ball[i] > 0:
        ans += 1
print(ans)
