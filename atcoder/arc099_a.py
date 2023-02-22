import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(math.ceil(N/(K-1)))
