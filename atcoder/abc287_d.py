def match(s, t, i):
    return s[i] == "?" or t[i] == "?" or s[i] == t[i]

S = input()
T = input()
lens = len(S)
lent = len(T)

S2 = list(S[-lent:])
# print("S2=", "".join(S2))
memo = [False]*lent
fcnt = 0
for i in range(lent):
    if match(S2, T, i):
        memo[i] = True
    else:
        fcnt += 1
if fcnt == 0:
    print("Yes")
else:
    print("No")

for x in range(1, lent+1):
    S2[x-1] = S[x-1]
    if memo[x-1]:
        if match(S2, T, x-1):
            pass
        else:
            memo[x-1] = False
            fcnt += 1
    else:
        if match(S2, T, x-1):
            memo[x-1] = True
            fcnt -= 1
        else:
            pass
    # print("S2=", "".join(S2))
    if fcnt == 0:
        print("Yes")
    else:
        print("No")