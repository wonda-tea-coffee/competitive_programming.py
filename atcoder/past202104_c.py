N, M = map(int, input().split())
A = []
for i in range(N):
    k, *a = map(int, input().split())
    A.append(set(a))

P, Q = map(int, input().split())
B = set(map(int, input().split()))

ans = 0
for i in range(N):
    if len(A[i] & B) >= Q:
        ans += 1

print(ans)
