m = int(input())
mps = []
for _ in range(m):
    mps.append(tuple(map(int, input().split())))
n = int(input())
nps = set()
for _ in range(n):
    nps.add(tuple(map(int, input().split())))

# 基準はどこでもいい
mx = mps[0][0]
my = mps[0][1]

for npx, npy in nps:
    dx = npx - mx
    dy = npy - my
    res = True
    for mx2, my2 in mps:
        if not (mx2 + dx, my2 + dy) in nps:
            res = False
            break
    if res:
        print(dx, dy)
        break
