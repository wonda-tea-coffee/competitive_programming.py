def factor(n):
    div = []
    d = 2
    m = n
    while d * d <= n:
        while m % d == 0:
            m //= d
            div.append(d)
        d += 1
    if m > 1:
        div.append(m)

    if n == m:
        return [n]
    else:
        return div

N = int(input())
print("%d:" % N, *factor(N))