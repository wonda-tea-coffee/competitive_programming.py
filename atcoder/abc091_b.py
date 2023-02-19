N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
ans = 0
for i in range(N):
    ans = max(ans, s.count(s[i]) - t.count(s[i]))
print(ans)
