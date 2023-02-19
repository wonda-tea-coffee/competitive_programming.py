N = int(input())
P = list(map(int, input().split()))
ans = 0
minnum = P[0]
for i in range(N):
    if P[i] <= minnum:
        ans += 1
        # print(i+1, P[i])

    minnum = min(minnum, P[i])
print(ans)
