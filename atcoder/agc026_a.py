N = int(input())
a = list(map(int, input().split()))
ans = 0
c = -1
l = 0
for ai in a:
    if c == ai:
        l += 1
    else:
        ans += l // 2
        l = 1
        c = ai

print(ans + l // 2)