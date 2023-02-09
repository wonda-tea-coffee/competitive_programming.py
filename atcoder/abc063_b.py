S = input()
ls = len(S)
if ls == len(set(S)):
    print("yes")
else:
    print("no")
