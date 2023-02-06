N = int(input())
S = input()
while S.count("na") > 0:
    S = S.replace("na", "nya")
print(S)