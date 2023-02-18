def is_prime(n):
    if n == 1: return False
    if n > 2 and n % 2 == 0: return False

    d = 3
    while d * d <= n:
        if n % d == 0: return False
        d += 2
    return True

def is_like2017(n):
    assert n % 2 == 1
    return is_prime(n) and is_prime((n+1)//2)

Q = int(input())
l = []
r = []
for _ in range(Q):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

M = max(r)
memo = [0]*(M+1)
cnt = 0
for i in range(1, M+1):
    if i % 2 == 1 and is_like2017(i):
        cnt += 1
    memo[i] = cnt

for i in range(Q):
    print(memo[r[i]] - memo[l[i]-1])
