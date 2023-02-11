import math

N = int(input())

# S = 3^0 + 3^1 + 3^2 + ... + 3^k
# 3S = 3^1 + 3^1 + 3^2 + ... + 3^(k+1)
# 2S = 3^(k+1) - 1
#  S = (3^(k+1) - 1)/2
# (3^(k+1) - 1)/2 >= N
# 3^(k+1) - 1 >= 2N
# 3^(k+1) >= 2N + 1
# k+1 >= math.log(2N + 1, 3)
# k = math.ceil(math.log(2N + 1, 3)) - 1

ans = []
L = N
while L != 0:
    k = math.ceil(math.log(2*abs(L) + 1, 3)) - 1
    n = 3**k
    if L < 0:
        n *= -1
    ans.append(n)
    # print(N, k, n, ans)
    L -= n

M = len(ans)
print(M)
print(*ans)

assert 1 <= M <= 100
assert sum(ans) == N
assert len(set(map(abs, ans))) == M
