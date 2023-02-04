N, P = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for ai in A:
    if ai < P: ans += 1

print(ans)
