X, A, B, C = map(int, input().split())

th = X/A + C
tt = X/B

if th == tt:
    print("Tie")
elif th > tt:
    print("Tortoise")
else:
    print("Hare")
