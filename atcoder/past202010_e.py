from itertools import permutations

N = int(input())
S = input()
sl = list(S)
revs = "".join(reversed(sl))

for t in permutations(sl):
    u = "".join(t)
    if u != S and u != revs:
        exit(print(u))
print("None")