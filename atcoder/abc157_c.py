N, M = map(int, input().split())
ans = [-1]*N
for _ in range(M):
    s, c = map(int, input().split())
    s -= 1
    if (ans[s] != -1 and ans[s] != c) or (N > 1 and s == 0 and c == 0):
        print(-1)
        exit()
    else:
        ans[s] = c

if ans[0] == -1:
    if N > 1:
        ans[0] = 1
    else:
        ans[0] = 0
for i in range(1, N):
    if ans[i] == -1:
        ans[i] = 0
print("".join(map(str, ans)))
