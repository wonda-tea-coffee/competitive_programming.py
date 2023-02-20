N, M = map(int, input().split())
C = []
for _ in range(N):
    a, b = map(int, input().split())
    C.append((a, b))
C.sort()
cnt = 0
ans = 0
for a, b in C:
    # print(a, b)
    if cnt + b <= M:
        cnt += b
        ans += a * b
    elif cnt + b > M:
        ans += a * (M - cnt)
        break

print(ans)
