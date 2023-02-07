import copy
import sys

S = input()
T = input()
if S == T:
    print("Yes")
    sys.exit(0)

S = list(S)
for i in range(1, len(S)):
    SS = copy.deepcopy(S)
    SS[i-1], SS[i] = SS[i], SS[i-1]
    if "".join(SS) == T:
        print("Yes")
        sys.exit(0)

print("No")