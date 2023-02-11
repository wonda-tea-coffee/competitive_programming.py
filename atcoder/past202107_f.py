def is_booking(si, ti, sj, tj):
    # print(si, ti, sj, tj)
    l = len(set(range(si, ti+1)) & set(range(sj, tj+1)))
    return l > 1

N = int(input())
h = {}
for _ in range(N):
    d, s, t = map(int, input().split())
    if d in h:
        h[d].append((t, s))
    else:
        h[d] = [(t, s)]

for key in h:
    h[key].sort()
    l = len(h[key])
    for i in range(1, l):
        if is_booking(h[key][i][1], h[key][i][0], h[key][i-1][1], h[key][i-1][0]):
            print("Yes")
            exit()

print("No")
