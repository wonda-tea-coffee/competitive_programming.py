S = input()
if S.count("C") == 0 or S.count("F") == 0 or S.index("C") > S.rindex("F"):
    print("No")
else:
    print("Yes")