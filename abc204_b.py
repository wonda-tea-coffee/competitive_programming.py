input()
A = list(map(int, input().split()))
ans = 0
for ai in A:
    if ai > 10:
        ans += ai - 10
print(ans)
