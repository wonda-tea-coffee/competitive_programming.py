S = input()
for a, b in [("N", "S"), ("W", "E")]:
    if (a in S and not b in S) or (not a in S and b in S):
        print("No")
        exit()
print("Yes")