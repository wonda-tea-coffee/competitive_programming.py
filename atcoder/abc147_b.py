S = input()
ls = len(S)
ans = 0

for i in range(ls//2):
    if S[i] != S[ls-i-1]:
        ans += 1

print(ans)
