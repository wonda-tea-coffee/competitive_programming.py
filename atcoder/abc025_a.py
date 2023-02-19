import itertools

S = list(input())
N = int(input())

for i, a in enumerate(itertools.product(S, repeat=2), 1):
    if i == N:
        print("".join(a))
        exit()