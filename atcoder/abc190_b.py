N, S, D = map(int, input().split())

ans = False
for i in range(N):
    x, y = map(int, input().split())
    if x < S and y > D:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
