import sys
from itertools import combinations

a = [int(input()) for _ in range(5)]
k = int(input())

for ai, aj in combinations(a, 2):
    if abs(ai - aj) > k:
        print(":(")
        sys.exit(0)

print("Yay!")
