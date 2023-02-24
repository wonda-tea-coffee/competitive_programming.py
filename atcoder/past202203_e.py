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

def normalize(y, m, d):
    return "%04d/%02d/%02d" % (y, m, d)

def is_good(y, m, d):
    return len(set(normalize(y, m, d))) <= 3 # /を含む

y, m, d = map(int, input().split("/"))

while not is_good(y, m, d):
    y, m, d = nextday(y, m, d)

print(normalize(y, m, d))
