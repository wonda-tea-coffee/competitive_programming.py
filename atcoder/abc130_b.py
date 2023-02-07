N, X = map(int, input().split())
L = list(map(int, input().split()))
d = 0
ans = 1

for i in range(N):
    nd = d + L[i]
    if nd <= X:
        ans += 1
    d = nd

print(ans)