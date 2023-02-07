import re

if re.fullmatch(r"[A-Z][1-9][0-9]{5}[A-Z]", input()):
    print("Yes")
else:
    print("No")