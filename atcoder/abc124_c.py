S = list(map(bool, map(int, input())))
ans = 0
f = S[0]
for i in range(len(S)):
    if S[i] != f: ans += 1
    f = not f
print(ans)
# 10101110101001000110
# 10101010101010101010