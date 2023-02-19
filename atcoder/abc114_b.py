S = input()
ls = len(S)
ans = 10**100
for i in range(ls-2):
    ans = min(ans, abs(753 - int(S[i:i+3])))
print(ans)
