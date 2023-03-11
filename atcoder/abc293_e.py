from functools import lru_cache

A, X, M = map(int, input().split())

@lru_cache(maxsize=None)
def f(x):
    if x <= 1: return x
    elif x % 2 == 0:
        r = x//2
        return ((1 + pow(A,r,M)) * f(r)) % M
    else:
        return (f(x-1)*A + 1) % M

print(f(X))
