S = input()
ls = len(S)

if S.count("post") > 0:
    pi = S.index("post")
    print(pi // 4 + 1)
else:
    print("none")