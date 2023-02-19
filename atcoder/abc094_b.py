import bisect

N, M, X = map(int, input().split())
A = list(map(int, input().split()))

i = bisect.bisect_left(A, X)
print(min(i, M-i))
