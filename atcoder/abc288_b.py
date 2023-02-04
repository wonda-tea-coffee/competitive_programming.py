N, K = map(int, input().split())
S = []
for _ in range(K):
    S.append(input())

S.sort()
for si in S:
    print(si)
