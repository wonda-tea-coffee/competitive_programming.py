import sys
sys.setrecursionlimit(1000000)

N = int(input())
nums = set()

def dfs(n):
    sn = str(n)
    if "3" in sn and "5" in sn and "7" in sn:
        nums.add(n)

    for i in [3, 5, 7]:
        m = n * 10 + i
        if m <= N:
            dfs(m)

dfs(0)

print(len(nums))
