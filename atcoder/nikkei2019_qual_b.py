N = int(input())
S = [input() for _ in range(3)]
ans = 0

for i in range(N):
    s = set()
    for j in range(3):
        s.add(S[j][i])
    ans += len(s) - 1

print(ans)