# 3点が一直線上に並んでいるか
def is_alignment(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1]) == 0

# 3点から成る三角形の面積
# https://atcoder.jp/contests/abc224/editorial/2810
def area_of_triangle_3p(a, b, c):
    return abs((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1]))/2
