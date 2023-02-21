N = int(input())
Q = []
for _ in range(N):
    a, b = map(int, input().split())
    Q.append((-a-b, a, b))
Q.sort()

takahashi = 0
aoki = 0
for i in range(N):
    if i % 2 == 0:
        takahashi += Q[i][1]
    else:
        aoki += Q[i][2]
print(takahashi - aoki)
