N = int(input())
H = list(map(int, input().split()))
ans = 0
h = -1
for i in range(N):
    if H[i] >= h:
        h = H[i]
        ans += 1

print(ans)