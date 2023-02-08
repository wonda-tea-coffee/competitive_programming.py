# 1 -> 2(1)
# -3 -> -1 ->(2)
# -1 -> 1
A, B = map(int, input().split())
ans = B - A
if A < 0 and B > 0:
    ans -= 1
print(ans)