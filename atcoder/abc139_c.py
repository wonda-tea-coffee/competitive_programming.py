N = int(input())
H = list(map(int, input().split()))
h = float("inf")
ans = 0
cnt = 0
for i in range(N-1, -1, -1):
    if h <= H[i]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    h = H[i]
print(max(ans, cnt))
