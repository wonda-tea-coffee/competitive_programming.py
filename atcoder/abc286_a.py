N, P, Q, R, S = map(int, input().split())
P -= 1
Q -= 1
R -= 1
S -= 1
A = list(map(int, input().split()))

i = 0
while P + i <= Q:
    A[P + i], A[R + i] = A[R + i], A[P + i]
    i += 1

print(' '.join(list(map(str, A))))
