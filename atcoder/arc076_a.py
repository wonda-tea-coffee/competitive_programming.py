def modpow(a, b, m):
    ret = 1
    k = a
    while b > 0:
        if b & 1:
            ret = ret * k % m
        k = k**2 % m
        b //= 2

    return ret

N, M = map(int, input().split())

if abs(N-M) > 1:
    print(0)
    exit()

MOD = 10**9+7
L = max(N, M)
fact = [0]*(L+1)
fact[0] = 1
for i in range(1, L+1):
    fact[i] = i * fact[i-1] % MOD

ans = fact[N] * fact[M]
if M == N:
    ans *= 2
print(ans % MOD)
