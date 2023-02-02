import sys
input = lambda: sys.stdin.readline().rstrip()

h = {}
for i in range(1, 6):
    h[str(i)] = 0
for i in range(6, 11):
    h[str(i%10)] = 1

ans = 500
N = input()

for i in range(1, len(N)):
    if N[i-1] == N[i]:
        ans += 301
    elif h[N[i-1]] == h[N[i]]:
        ans += 210
    else:
        ans += 100

print(ans)
