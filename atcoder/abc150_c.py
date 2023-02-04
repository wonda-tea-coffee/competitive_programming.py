import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
pi = -1
qi = -1
for i, x in enumerate(itertools.permutations(list(range(1, N+1)))):
    if x == P:
        pi = i+1
    if x == Q:
        qi = i+1

# print(pi, qi)
print(abs(pi - qi))