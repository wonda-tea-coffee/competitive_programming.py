import sys

N = int(input())

st, sx, sy = 0, 0, 0

s = []
for _ in range(N):
    s.append(tuple(map(int, input().split())))

for i in range(N):
    nt, nx, ny = s[i]
    d = abs(nx-sx) + abs(ny-sy)
    t = nt-st
    if t < d or (t - d) % 2 == 1:
        print("No")
        sys.exit(0)
    
    st, sx, sy = nt, nx, ny

print("Yes")
