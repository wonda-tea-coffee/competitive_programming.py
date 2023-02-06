H, W = map(int, input().split())
ans = [0] * W
for _ in range(H):
    s = input()
    for i in range(W):
        if s[i] == "#":
            ans[i] += 1

print(*ans)