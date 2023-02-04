S = input()

while S:
    res = False

    for s in ["dream", "dreamer", "erase", "eraser"]:
        if S.endswith(s):
            S = S[:len(S)-len(s)]
            res = True
            break
            # print(s, S)

    if not res: break

if S == "":
    print("YES")
else:
    print("NO")
