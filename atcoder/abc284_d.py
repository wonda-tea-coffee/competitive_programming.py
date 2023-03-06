import sys
input = lambda: sys.stdin.readline().rstrip()

# エラトステネスの篩
# n以下の素数を求める
def eratosthenes(n):
    isprime = ([False, True]*(n//2+1))[:n+1]
    isprime[1] = False
    isprime[2] = True

    for i in range(3, int(n**.5)+1, 2):
        if not isprime[i]: continue
        for j in range(i*i, n+1, i):
            isprime[j] = False
    return isprime

isprime = eratosthenes(2_080_083)
T = int(input())
for _ in range(T):
    N = int(input())
    d = 2
    for d in range(2, N+1):
        if not isprime[d]: continue
        if N % d > 0: continue
        if N % (d*d) == 0:
            print(d, N//(d*d))
        else:
            print(int((N//d)**0.5), d)
        break
