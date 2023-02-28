N = int(input())
ans = [-1]*6
for i in range(1, N+1):
    p, v = input().split()
    if v == "WA": continue

    n = ord(p)-65
    if ans[n] == -1:
        ans[n] = i

for a in ans:
    print(a)