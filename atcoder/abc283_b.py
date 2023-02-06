N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    t, *s = map(int, input().split())
    if t == 1:
        k, x = s
        A[k-1] = x
    else:
        k = s[0]
        print(A[k-1])
