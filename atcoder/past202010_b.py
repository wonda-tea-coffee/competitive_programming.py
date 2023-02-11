X, Y = map(int, input().split())

if Y == 0:
    print("ERROR")
else:
    r = str(X/Y).split(".")
    if len(r[1]) == 1:
        r[1] += "0"
    print(r[0] + "." + r[1][:2])