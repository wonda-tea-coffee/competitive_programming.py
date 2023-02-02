import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    c = b - a
    if c % 100 >= 50: ans += 1
    if c % 10 >= 5: ans += 1

print(ans)
