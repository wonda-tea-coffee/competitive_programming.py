
def is_leap(y):
    if y % 400 == 0: return True
    if y % 100 == 0: return False
    return y % 4 == 0

def is_lastday(y, m, d):
    if m == 2 and is_leap(y): return d == 29
    return lastday[m] == d

def nextday(y, m, d):
    if not is_lastday(y, m, d): return y, m, d+1
    if m != 12: return y, m+1, 1
    return y+1, 1, 1

lastday = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

sy, sm, sd = map(int, input().split("-"))
ty, tm, td = map(int, input().split("-"))

iy, im, id = 2022, 1, 1
week = 0 # 0, 1が土日とする
while (iy, im, id) != (sy, sm, sd):
    iy, im, id = nextday(iy, im, id)
    week = (week + 1) % 7

ans = 0
while True:
    if week == 0 or week == 1: ans += 1
    if (iy, im, id) == (ty, tm, td): break
    iy, im, id = nextday(iy, im, id)
    week = (week + 1) % 7

print(ans)
