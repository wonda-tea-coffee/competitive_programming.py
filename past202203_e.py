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

def is_good(s):
    return len(set("".join(s.split("/")))) <= 2

S = input()
while True:
    y, m, d = map(int, S.split("/"))
    s = "%04d/%02d/%02d" % (y, m, d)

    if is_good(s):
        print(s)
        break

    ny, nm, nd = next_day(y, m, d)
    S = "%04d/%02d/%02d" % (ny, nm, nd)
