import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = [0] + list(map(int, input().split()))

memo = {}
def solve(k):
    if k in memo: return memo[k]
    if k == 1: return 0

    if k % 2 == 0:
        ret = solve(A[k//2]) + 1
    else:
        ret = solve(A[(k-1)//2]) + 1

    memo[k] = ret
    return ret

for k in range(1, 2*N+2):
    print(solve(k))
