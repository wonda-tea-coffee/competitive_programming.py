import math

A, B, C, D = map(int, input().split())

# A + B*K <= C*K*D
# B*K - C*D*K <= -A
# C*D*K - B*K >= A
# K*(C*D - B) >= A
# K >= A/(C*D - B)

if C*D > B:
    print(math.ceil(A / (C*D - B)))
else:
    print(-1)
