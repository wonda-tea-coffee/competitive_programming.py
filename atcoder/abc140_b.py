N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
mae = -10**100
for i in range(N):
    ans += B[A[i]]
    if mae + 1 == A[i]:
        ans += C[A[i]-1]
    mae = A[i]

print(ans)