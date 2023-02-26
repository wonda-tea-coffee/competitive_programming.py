import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
N = int(input())
ratio = [0]*(T+1)
for _ in range(N):
    L, R = map(int, input().split())
    ratio[L] += 1
    ratio[R] -= 1

ans = 0
for i in range(T):
    ans += ratio[i]
    print(ans)
