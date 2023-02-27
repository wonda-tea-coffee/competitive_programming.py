import bisect

N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))

print(bisect.bisect_left(A, X))
