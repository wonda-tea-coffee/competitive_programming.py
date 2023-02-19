N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = -1
val = float("inf")
for i in range(N):
    v = abs(A - (T - H[i] * 6 / 1000))
    if val > v:
        val = v
        ans = i+1
print(ans)