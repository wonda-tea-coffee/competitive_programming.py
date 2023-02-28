N = int(input())
ans = 0

for _ in range(N):
    A, B = map(int, input().split())
    C = (B - A) % 100
    if C >= 50: ans += 1
    if C % 10 >= 5: ans += 1

print(ans)
