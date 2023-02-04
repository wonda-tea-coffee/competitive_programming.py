import string
import sys
from collections import defaultdict

S = sys.stdin.read()

h = defaultdict(int)
for si in list(S):
    key = si
    if "a" <= si and si <= "z":
        pass
    elif "A" <= si and si <= "Z":
        key = si.lower()
    else:
        continue

    h[key] += 1

for a in list(string.ascii_lowercase):
    print("%s : %d" % (a, h[a]))
