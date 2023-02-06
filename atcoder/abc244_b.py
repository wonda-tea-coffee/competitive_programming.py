N = int(input())
T = input()
x = 0
y = 0
cd = 0
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for i in range(N):
    if T[i] == "S":
        x += d[cd][0]
        y += d[cd][1]
    else:
        cd = (cd + 1) % 4

print(x, y)