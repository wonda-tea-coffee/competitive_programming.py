from itertools import permutations

S, K = input().split()
K = int(K)
p = sorted(list(set(permutations(S))))
print("".join(p[K-1]))
