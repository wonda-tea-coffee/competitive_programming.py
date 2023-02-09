def d(n, k):
    a = n // k
    return k*a*(a+1)//2

N = int(input())
print(N*(N+1)//2 - (d(N, 3) + d(N, 5) - d(N, 15)))