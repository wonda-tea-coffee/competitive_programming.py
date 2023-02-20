N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ans = 0

for i in range(N):
    v = sum(A1[:i+1]) + sum(A2[i:])
    ans = max(ans, v)
print(ans)
