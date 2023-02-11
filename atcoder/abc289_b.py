N, M = map(int, input().split())
a = list(map(int, input().split()))

re = [False] * (N+1)
for ai in a:
    re[ai] = True
ans = []
i = 1
j = 1
while i <= N:
    while re[j]:
        j += 1
    k = j
    while k >= i:
        ans.append(k)
        k -= 1
    j += 1
    i = j

print(*ans)
