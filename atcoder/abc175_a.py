S = input()
if S == "RRR":
    print(3)
elif S.count("RR") > 0:
    print(2)
elif S.count("R") > 0:
    print(1)
else:
    print(0)