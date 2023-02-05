S = sorted(list(input()))
if S.count(S[0]) == S.count(S[-1]) == 2:
    print("Yes")
else:
    print("No")