N, X = map(int, input().split())
X -= 1
A = list(map(lambda x: int(x)-1, input().split()))
B = [False] * N
ans = 0

i = X
while not B[i]:
    B[i] = True
    ans += 1
    i = A[i]

print(ans)
