from itertools import *

N = int(input())
A = list(map(int, input().split()))

for a in combinations(A, 3):
    if sum(a) == 1000:
        print("Yes")
        exit()

print("No")