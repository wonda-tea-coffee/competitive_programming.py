N, L = map(int, input().split())
diff = 10**100
ans = None

umami_all = N*L + N*(N+1)//2 - N
for i in range(1, N+1):
    umami_part = umami_all - (L + i - 1)
    d = abs(umami_all - umami_part)
    if d < diff:
        diff = d
        ans = umami_part

print(ans)
