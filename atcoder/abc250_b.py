N, H, W = map(int, input().split())

for i in range(N*H):
    ty = i // H
    for j in range(N*W):
        tx = j // W
        if (ty + tx) % 2 == 0:
            c = "."
        else:
            c = "#"

        print(c, end="")
    print()
