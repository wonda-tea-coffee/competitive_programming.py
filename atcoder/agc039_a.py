from itertools import groupby

S = input()
K = int(input())

X = [len(list(v)) for _, v in groupby(S)]
if len(X) == 1:
    print(X[0]*K//2)
elif S[0] != S[-1]:
    print(sum(map(lambda x: x//2*K, X)))
else:
    ans = X[0]//2 + X[-1]//2 + (X[0]+X[-1])//2*(K-1)
    for l in X[1:-1]:
        ans += l//2*K
    print(ans)
