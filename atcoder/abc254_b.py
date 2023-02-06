import math

N = int(input())
for i in range(N):
    for j in range(i+1):
        print(math.comb(i, j), end=" ")
    print()
