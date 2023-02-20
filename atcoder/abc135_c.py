N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    m1 = min(A[i], B[i])
    ans += m1
    A[i] -= m1
    B[i] -= m1

    if B[i] > 0:
        m2 = min(A[i+1], B[i])
        ans += m2
        A[i+1] -= m2
print(ans)
