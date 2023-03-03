H, W = map(int, input().split())
S = [input() for _ in range(H)]

c = sum(map(lambda x: x.count("#"), S))
print("Possible" if c == H+W-1 else "Impossible")
