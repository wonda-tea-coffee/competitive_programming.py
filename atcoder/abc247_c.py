memo = {}
def s(n):
    if n in memo: return memo[n]
    if n == 1: return [1]

    ret = s(n-1) + [n] + s(n-1)
    memo[n] = ret
    return ret

N = int(input())
print(*s(N))
