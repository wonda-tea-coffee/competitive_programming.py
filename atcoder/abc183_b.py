sx, sy, gx, gy = map(int, input().split())

if sy == -gy or -sy == gy:
    print((sx+gx)/2)
else:
    print((sx*gy + sy*gx)/(sy + gy))
