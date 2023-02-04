while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0: break

    for i in range(h):
        f = i % 2 == 0
        for j in range(w):
            if f:
                print("#", end="")
            else:
                print(".", end="")
            f = not f
        print()
    print()
