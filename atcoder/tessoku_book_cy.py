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

N = int(input())
isprime = eratosthenes(N)
for i in range(1, N+1):
    if isprime[i]:
        print(i)
