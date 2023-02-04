def modpow(a, b, m):
    ret = 1
    k = a
    while b > 0:
        if b & 1:
            ret = ret * k % m
        k = k**2 % m
        b //= 2

    return ret

def comb(n, r, m):
    a = fact[n]
    b = fact[r] * fact[n - r] % m
    return a * modpow(b, m - 2, m) % m

N, K = map(int, input().split())
M = 998244353
A = list(map(int, input().split()))
A.sort(reverse=True)

fact = [0] * (N+1)
fact[0] = 1
for i in range(1, N+1):
    fact[i] = i * fact[i - 1] % M

a = 0
j = 0
for i in range(N-1, K-2, -1):
    a = (a + A[j]*comb(i, K-1, M) - A[N-1-j]*comb(i, K-1, M)) % M
    j += 1

print(a * fact[K] * fact[N-K] * modpow(fact[N], M-2, M) % M)
