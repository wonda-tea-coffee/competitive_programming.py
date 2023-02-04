# cがd個続く数(mod m)
def cd(c, d, m):
    # S = c*10**0 + c*10**1 + ... + c*10**(d-1)
    # 10S = c*10**1 + c*10**2 + ... + c*10**d
    # 9S = c*10**d - c*10**0
    # 9S = c*10**d - c
    # 9S = c(10**d - 1)
    #  S = c(10**d - 1)/9
    return c * (pow(10, d, m) - 1) * pow(9, -1, m) % m

K, M = map(int, input().split())

C = [0]*K
D = [0]*K
length = 0
for i in range(K):
    C[i], D[i] = map(int, input().split())
    length += D[i]

ans = 0
l = 0
for i in range(K):
    l += D[i]
    k = cd(C[i], D[i], M) * pow(10, length-l, M) % M
    ans = (ans + k) % M

print(ans)
