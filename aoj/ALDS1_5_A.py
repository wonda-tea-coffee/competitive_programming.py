import sys
sys.setrecursionlimit(1000000)

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

maked = set()
def dfs(i, s):
    maked.add(s)
    if i == n: return

    dfs(i+1, s)
    dfs(i+1, s+A[i])

dfs(0, 0)
for mi in m:
    if mi in maked:
        print("yes")
    else:
        print("no")
