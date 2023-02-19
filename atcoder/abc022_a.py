N, S, T = map(int, input().split())
W = int(input())

if S <= W <= T:
    ans = 1
else:
    ans = 0

for _ in range(N-1):
    W += int(input())
    if S <= W <= T:
        ans += 1
print(ans)
