N = int(input())
S = input()
ls = len(S)
if ls % 2 == 0 and S[:ls//2] == S[ls//2:]:
    print("Yes")
else:
    print("No")