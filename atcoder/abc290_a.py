N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(lambda x: int(x)-1, input().split()))
ans = 0
for i in range(M):
    ans += A[B[i]]
print(ans)