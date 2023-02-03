import math

N = int(input())

# N <= K(K+1)/2
# K^2 + K - 2N >= 0
# K = (-1+√(1+8N))/2
print(
    math.ceil(
        (math.sqrt(1+8*N) - 1)/2
    )
)
