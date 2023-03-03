S = list(input())
ans = 0
for i, si in enumerate(S[::-1]):
    ans += 26**i * (ord(si) - 64)
print(ans)
