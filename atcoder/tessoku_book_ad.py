def modpow(a, b):
    ret = 1
    k = a
    while b > 0:
        if b & 1:
            ret = ret * k % MOD
        k = k*k % MOD
        b //= 2

    return ret

def comb(n, r):
    a = fact[n]
    b = fact[r] * fact[n-r] % MOD
    return a * modpow(b, MOD-2) % MOD

n, r = map(int, input().split())
MOD = 1000000007

fact = [0]*(n+1)
fact[0] = 1
for i in range(1, n+1):
    fact[i] = i * fact[i-1] % MOD

print(comb(n, r))
