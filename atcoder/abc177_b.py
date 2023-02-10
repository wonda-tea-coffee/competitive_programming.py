S = list(input())
T = list(input())
lens = len(S)
lent = len(T)
ans = 10**100
for i in range(lens-lent+1):
    ng = 0
    for j in range(lent):
        if S[i+j] != T[j]:
            ng += 1
    ans = min(ans, ng)

print(ans)
