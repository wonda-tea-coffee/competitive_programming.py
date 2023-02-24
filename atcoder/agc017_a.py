N, P = map(int, input().split())
A = list(map(lambda x: int(x)%2, input().split()))

even = A.count(0)
odd = N-even

if odd > 0:
    print(2**(even+odd-1))
elif P == 1:
    print(0)
else:
    print(2**even)
