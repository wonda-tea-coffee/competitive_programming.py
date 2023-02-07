R, C = map(int, input().split())
for i in range(1, 9):
    if R == i or C == i or R == 16-i or C == 16-i:
        if i % 2 == 1:
            print("black")
        else:
            print("white")
        break
