import sys
sys.setrecursionlimit(1000000)

def dfs(i, s):
    # print(i, s)
    if i == 9:
        all.append(s)
        return

    # assert i <= 8 and len(s) <= 9

    if i == 0:
        for j in range(1, 10):
            dfs(i+1, str(j))
    elif i == 1 or i == 5 or i == 8:
        h = {1: 0, 5: 4, 8: 6}
        dfs(i+1, s + s[h[i]])
    else:
        for j in range(10):
            dfs(i+1, s + str(j))

N = int(input())
all = []
dfs(0, "")
all.sort()
print(all[N-1])