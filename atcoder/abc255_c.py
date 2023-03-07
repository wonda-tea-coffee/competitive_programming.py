X, A, D, N = map(int, input().split())

if D == 0:
    print(abs(X-A))
    exit()

first = A
last = A+(N-1)*D

if D < 0:
    first, last = last, first
    D = -D

if X <= first:
    print(first-X)
elif X >= last:
    print(X-last)
else:
    ans = D

    num = X
    while True:
        if (num-A)%D == 0:
            ans = min(ans, num-X)
            break
        else:
            num += 1

    num = X
    while True:
        if (num-A)%D == 0:
            ans = min(ans, X-num)
            break
        else:
            num -= 1

    print(ans)