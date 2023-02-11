import sys
sys.setrecursionlimit(1000000)

N = int(input())
S = []
for _ in range(N):
    S.append(set(input()))

def dfs(i, j, t):
    if len(t) == N:
        print(t)
        exit()

    if not (S[i] & S[j]):
        print(-1)
        exit()

    for s in list(S[i] & S[j]):
        dfs(i-1, j+1, s + t + s)

if N % 2 == 1:
    dfs(N//2-1, N//2+1, list(S[N//2])[0])
else:
    dfs(N//2-1, N//2, "")

print(-1)
