import sys
import string

S = input()

res = False
for s in list(string.ascii_lowercase):
    res |= S.count(s) > 0

if not res:
    print("No")
    sys.exit(0)

res2 = False
for s in list(string.ascii_uppercase):
    res2 |= S.count(s) > 0

if not res2:
    print("No")
    sys.exit(0)

if len(S) == len(set(S)):
    print("Yes")
else:
    print("No")
