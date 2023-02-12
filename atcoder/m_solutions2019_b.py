S = list(input())
K = len(S)

S += ["o"]*(15-K)
if S.count("o") >= 8:
    print("YES")
else:
    print("NO")