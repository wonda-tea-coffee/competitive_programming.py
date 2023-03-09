N = int(input())
a = [0] + list(map(int, input().split()))

c = 0
for i in range(1, N+1):
    if a[i] == i:
        c += 1

ans = c*(c-1)//2
for i in range(1, N+1):
    j = a[i]
    if j > i and a[j] == i:
        ans += 1

print(ans)
