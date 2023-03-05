N = int(input())
A = [list(map(int, list(input()))) for _ in range(N)]
ans = 0
for y in range(N):
    for x in range(N):
        for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            c = A[y][x]
            ny = y
            nx = x
            for k in range(N-1):
                ny = (ny+dy)%N
                nx = (nx+dx)%N
                c = c*10 + A[ny][nx]
            ans = max(ans, c)
print(ans)