N = int(input())
h = list(map(int, input().split()))
ans = 0
while max(h) > 0:
    l = 0
    while l < N and h[l] == 0:
        l += 1

    minh = 101
    r = l
    while r < N and h[r] > 0:
        minh = min(minh, h[r])
        r += 1

    ans += minh
    for i in range(l, r):
        h[i] -= minh

print(ans)
