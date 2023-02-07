S = input()
if S == "".join(reversed(list(S))):
    print("YES")
else:
    print("NO")