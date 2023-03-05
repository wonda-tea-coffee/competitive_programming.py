N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
ans = [-1]*N
si = -1
siv = 10**100
for i in range(N):
    if siv > T[i]:
        siv = T[i]
        si = i

ans[si] = siv
for i in range(N):
    j1 = (si+i)%N
    j2 = (si+i+1)%N
    ans[j2] = min(T[j2], ans[j1] + S[j1])

for i in range(N):
    print(ans[i])
