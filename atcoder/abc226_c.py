import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()

def solve(n):
    if remembered[n]: return 0

    ret = 0
    for ak in A[n]:
        ret += solve(ak)

    ret += T[n]
    remembered[n] = True
    return ret

N = int(input())
T = [-1]
A = [[]]
for _ in range(N):
    t, _, *ai = map(int, input().split())
    T.append(t)
    A.append(ai)
remembered = [False]*(N+1)

print(solve(N))
