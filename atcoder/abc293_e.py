from functools import lru_cache

A, X, M = map(int, input().split())

@lru_cache(maxsize=None)
def f(x):
    if x == 0:
        return 0
    elif x % 2 == 0:
        return f(x//2)*(1+pow(A,x//2,M)) % M
    else:
        return (f(x-1)*A + 1) % M

print(f(X))
