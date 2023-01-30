def is_leap(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    else:
        return y % 4 == 0

def next_day(y, m, d):
    ld = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(y):
        ld[2] += 1

    if d == ld[m]:
        d = 1
        m += 1
        if m == 13:
            m = 1
            y += 1
    else:
        d += 1

    return y, m, d

sy, sm, sd = map(int, input().split("-"))
ty, tm, td = map(int, input().split("-"))

ans = 0
ry, rm, rd = 2022, 1, 1
w = 0
while ry != sy or rm != sm or rd != sd:
    ry, rm, rd = next_day(ry, rm, rd)
    w = (w + 1) % 7

while True:
    # print(sy, sm, sd, w)
    if w == 0 or w == 1:
        ans += 1
    if sy == ty and sm == tm and sd == td:
        break

    sy, sm, sd = next_day(sy, sm, sd)
    w = (w + 1) % 7

print(ans)
