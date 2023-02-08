import re

N = input()
if re.search(r"(\d)\1\1", N):
    print("Yes")
else:
    print("No")