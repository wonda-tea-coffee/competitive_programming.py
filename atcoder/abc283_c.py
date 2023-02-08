S = input()
ans = 0
i = 0
ls = len(S)
while i < ls:
    if S[i] == "0" and i+1 < ls and S[i+1] == "0":
        i += 2
    else:
        i += 1
    ans += 1

print(ans)
