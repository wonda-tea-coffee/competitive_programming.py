# A <= B <= C
A, B, C = sorted(list(map(int, input().split())))
ans = C-B
A += C-B
B += C-B
# print(A, B, C)

if (B-A)%2 == 0:
    ans += (B-A)//2
else:
    ans += (B-A+3)//2

print(ans)
