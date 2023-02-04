A, B, C, X, Y = map(int, input().split())

# A+B, 2*C
m = min(X, Y)
ans = min(A+B, 2*C) * m
X -= m
Y -= m
if X > 0:
    if A < 2*C:
        ans += A*X
    else:
        ans += 2*C*X
else:
    if B < 2*C:
        ans += B*Y
    else:
        ans += 2*C*Y
print(ans)
