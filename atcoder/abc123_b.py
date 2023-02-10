A = []
for _ in range(5):
    a = int(input())
    if a % 10 == 0:
        b = 0
    else:
        b = 10 - a % 10
    A.append((b, a))
A.sort()
# print(A)
ans = 0
for i in range(4):
    ans += A[i][0] + A[i][1]

print(ans + A[-1][1])
