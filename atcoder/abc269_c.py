import sys
sys.setrecursionlimit(1000000)

s = list("{0:b}".format(int(input())))
ans = []

def dfs(i, t):
    if i == len(s):
        ans.append(t)
        return

    if s[i] == "0":
        dfs(i+1, t+"0")
    else:
        dfs(i+1, t+"0")
        dfs(i+1, t+"1")

dfs(0, "")

ans.sort()
for a in ans:
    print(int(a, 2))
