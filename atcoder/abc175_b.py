N = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if L[i] == L[j]: continue
        for k in range(j+1, N):
            if L[i] == L[k]: continue
            if L[j] == L[k]: continue
            if L[k] < L[i] + L[j] and L[i] < L[j] + L[k] and L[j] < L[i] + L[k]:
                # print(i+1, j+1, k+1)
                ans += 1

print(ans)