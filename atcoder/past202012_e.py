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
            if hanko[y][x] == '#':
                if (xmax < x): xmax = x
                if (xmin > x): xmin = x
                if (ymax < y): ymax = y
                if (ymin > y): ymin = y

    for x in range(xmin, xmax+1):
        s = ''
        for y in range(ymin, ymax+1):
            s += hanko[x][y]
        newhanko.append(s)
    return newhanko

def rotate(hanko):
    newhanko = []
    height = len(hanko)
    width = len(hanko[0])
    for y in range(width):
        s = ''
        for x in range(height):
            s = hanko[x][y] + s
        newhanko.append(s)
    return newhanko

def search(hanko, dodai):
    dx = len(dodai) - len(hanko)
    dy = len(dodai[0]) - len(hanko[0])
    for x in range(0, dx+1):
        for y in range(0, dy+1):
            if (stamp(hanko, dodai, x, y)):
                return True
    return False

def stamp(hanko, dodai, xpos, ypos):
    for x in range(0, len(hanko)):
        for y in range(0, len(hanko[0])):
            c1 = hanko[x][y]
            c2 = dodai[x+xpos][y+ypos]
            if (c1 == '#' and c2 == '#'):
                return False
    return True

hanko = shrink(hanko)

for _ in range(4):
    if search(hanko, dodai):
        print("Yes")
        exit()
    hanko = rotate(hanko)
print("No")
