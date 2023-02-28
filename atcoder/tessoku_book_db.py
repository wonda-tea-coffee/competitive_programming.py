def modpow(a, b, m):
    ret = 1
    k = a
    while b > 0:
        if b & 1:
            ret = ret * k % m
        k = k**2 % m
        b //= 2

    return ret

a, b = map(int, input().split())
print(modpow(a, b, 1000000007))
