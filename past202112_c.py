import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ans = {}
for i in range(1, N+1):
    p, v = input().split()

    if v == "AC" and not p in ans:
        ans[p] = i

for a in sorted(list(ans)):
    print(ans[a])
