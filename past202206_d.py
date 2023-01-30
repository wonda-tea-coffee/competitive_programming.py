import string
import sys
sys.setrecursionlimit(1000000)

N = int(input())
ab = set()
for i in range(N):
    a, b = input().split()
    ab.add((a, b))

S = input()
T = input()

def is_similar(u, v):
    return (u, v) in ab or (v, u) in ab

done = set()
def dfs(s, i):
    done.add((s, i))

    if len(S) == i:
        return True
    if s[i] == T[i]:
        return dfs(s, i+1)
    for c in list(string.ascii_lowercase):
        if not is_similar(s[i], c):
            continue
        ta = list(s)
        ta[i] = c
        t = ''.join(ta)
        if (t, i) in done:
            continue
        done.add((t, i))
        if dfs(t, i):
            return True
    return False

if dfs(S, 0):
    print("Yes")
else:
    print("No")
