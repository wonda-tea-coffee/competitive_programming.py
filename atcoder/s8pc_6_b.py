import statistics

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

meda = int(statistics.median(A))
medb = int(statistics.median(B))
# print(meda, medb)
ans = 0
for i in range(N):
    ans += abs(meda - A[i]) + B[i] - A[i] + abs(B[i] - medb)

print(ans)
