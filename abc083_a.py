A, B, C, D = map(int, input().split())
r = A+B-(C+D)
if r > 0:
    print("Left")
elif r == 0:
    print("Balanced")
else:
    print("Right")