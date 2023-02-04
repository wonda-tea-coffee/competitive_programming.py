N = int(input())
d = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i, N+1, i):
        d[j] += 1

ans = 0
# print(d)
for i in range(1, N+1):
    if i % 2 == 1 and d[i] == 8: ans += 1
print(ans)
