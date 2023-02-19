def is_prime(n):
    if n == 1: return False
    if n > 2 and n % 2 == 0: return False

    d = 3
    while d * d <= n:
        if n % d == 0: return False
        d += 2
    return True

X = int(input())
while not is_prime(X):
    X += 1
print(X)
