import re

S = input()
l = list("keyence")
for i in range(len(l)+1):
    reg = "".join(l[:i]) + ".*" + "".join(l[i:])
    if re.fullmatch(reg, S):
        print("YES")
        exit()
print("NO")
