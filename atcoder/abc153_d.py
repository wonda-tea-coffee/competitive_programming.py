memo = {}
def dfs(x):
    if x == 1: return 1
    if x in memo: return memo[x]
    memo[x] = dfs(x//2) * 2 + 1
    return memo[x]

print(dfs(int(input())))
