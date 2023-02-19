N = int(input())
A = list(map(int, input().split()))
suma = sum(A)
ans = 10**10
s = 0
for ai in A:
    s += ai
    ans = min(ans, abs(2*s - suma))

print(ans)