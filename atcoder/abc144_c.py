N = int(input())
ans = N-1
d = 2
while d * d <= N:
    if N % d == 0:
        # print(d, N//d)
        ans = min(ans, d-1 + N//d-1)
    d += 1

print(ans)