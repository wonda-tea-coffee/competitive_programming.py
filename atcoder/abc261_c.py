from collections import defaultdict

N = int(input())
d = defaultdict(int)
for _ in range(N):
    S = input()
    if d[S] == 0:
        print(S)
    else:
        print("%s(%d)" % (S, d[S]))
    d[S] += 1
