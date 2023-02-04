import sys
input = lambda: sys.stdin.readline().rstrip()

def check(A, K, al, ar):
    x = [0]*(ar-al+1)

    m = ar+1-K-l
    for xi in range(m+1):
        c = A[xi+l] - x[xi]
        for j in range(K):
            x[xi+j] += c

    # print(x, A[al:ar+1])
    return x == A[al:ar+1]

N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    l, r = map(lambda x: int(x)-1, input().split())
    if check(A, K, l, r):
        print("Yes")
    else:
        print("No")
