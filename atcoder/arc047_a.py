N, L = map(int, input().split())
S = input()
ans = 0
c = 1
for i in range(N):
    if S[i] == "+":
        if c == L:
            c = 1
            ans += 1
        else:
            c += 1
    else:
        c -= 1

print(ans)