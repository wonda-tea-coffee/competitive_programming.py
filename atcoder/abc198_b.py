import re
S = re.sub(r"0+$", "", input())

if S == "".join(list(reversed(S))):
    print("Yes")
else:
    print("No")