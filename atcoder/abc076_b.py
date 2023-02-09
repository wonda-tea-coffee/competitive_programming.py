N = int(input())
K = int(input())
l = []

def dfs(cnt, n):
    if cnt == N:
        l.append(n)
        return

    dfs(cnt + 1, n + K)
    dfs(cnt + 1, n * 2)

dfs(0, 1)

print(sorted(l)[0])