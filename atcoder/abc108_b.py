# 2次元平面上の2頂点から反時計回りに作られる正方形を成す、残りの2頂点を求める
x1, y1, x2, y2 = map(int, input().split())
dx = x2 - x1
dy = y2 - y1
print(x2 - dy, y2 + dx, x1 - dy, y1 + dx)