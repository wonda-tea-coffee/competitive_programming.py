import string
import sys
import copy

a = list(string.ascii_lowercase)

S = list(input())
T = input()
for k in range(26):
    S2 = copy.deepcopy(S)
    for i in range(len(S2)):
        ai = a.index(S2[i])
        S2[i] = a[(ai + k) % 26]
    if "".join(S2) == T:
        print("Yes")
        sys.exit(0)

print("No")