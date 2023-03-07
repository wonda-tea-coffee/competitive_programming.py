import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
T = [-1]
A = [[]]
for _ in range(N):
    t, _, *ai = map(int, input().split())
    T.append(t)
    A.append([-1] + ai)

needed = [False]*(N+1)
needed[-1] = True

for i in range(N, 0, -1):
    if not needed[i]: continue

    for aj in A[i]:
        needed[aj] = True

ans = 0
for i in range(1, N+1):
    if not needed[i]: continue
    ans += T[i]

print(ans)
