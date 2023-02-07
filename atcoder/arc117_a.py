A, B = map(int, input().split())
if A < B:
    ans = list(range(-B, 0, 1))
    C = -B*(B+1)//2
    for i in range(A-1):
        ans.append(i+1)
        C += i+1
else:
    ans = list(range(1, A+1))
    C = A*(A+1)//2
    for i in range(B-1):
        ans.append(-(i+1))
        C -= i+1

if C != 0:
    ans.append(-C)

print(*ans)
