N, K, Q = map(int, input().split())
C = [0]*N
for _ in range(Q):
    a = int(input())
    C[a-1] += 1

for i in range(N):
    if K - (Q - C[i]) > 0:
        print("Yes")
    else:
        print("No")
