H, W = map(int, input().split())
dodai = [input() for _ in range(H)]
hanko = [input() for _ in range(H)]

# ハンコの余分な部分を取り除く
def shrink(hanko):
    newhanko = []
    xmax = 0
    xmin = 99
    ymax = 0
    ymin = 99
    for y in range(H):
        for x in range(W):
            if (hanko[y][x] == '#'):
                if (xmax < x): xmax = x
                if (xmin > x): xmin = x
                if (ymax < y): ymax = y
                if (ymin > y): ymin = y

    for y in range(ymin, ymax+1):
        s = ''
        for x in range(xmin, xmax+1):
            s += hanko[y][x]
        newhanko.append(s)
    return newhanko

# ハンコを右に90度回す
def rotate(hanko):
    newhanko = []
    height = len(hanko)
    width = len(hanko[0])
    for x in range(width):
        s = ''
        for y in range(height):
            s = hanko[y][x] + s
        newhanko.append(s)
    return newhanko

def search(hanko, dodai):
    dy = len(dodai) - len(hanko)
    dx = len(dodai[0]) - len(hanko[0])
    for y in range(dy+1):
        for x in range(dx+1):
            if stamp(hanko, dodai, y, x):
                return True
    return False

# 土台の左上隅を決めてハンコを押せるかチェック
def stamp(hanko, dodai, ypos, xpos):
    for y in range(len(hanko)):
        for x in range(len(hanko[0])):
            c1 = hanko[y][x]
            c2 = dodai[y+ypos][x+xpos]
            if c1 == '#' and c2 == '#':
                return False
    return True

hanko = shrink(hanko)

for _ in range(4):
    if search(hanko, dodai):
        print("Yes")
        exit()
    hanko = rotate(hanko)

print("No")
