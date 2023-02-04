N, X = map(int, input().split())
A = list(map(int, input().split()))

s = 0
for i in range(N):
    if i % 2 == 0:
        s += A[i]
    else:
        s += A[i]-1

if s <= X:
    print("Yes")
else:
    print("No")