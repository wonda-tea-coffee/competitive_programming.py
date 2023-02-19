N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    B.append((A[i], i+1))
B.sort()

print(*list(map(lambda x: x[1], B)))
