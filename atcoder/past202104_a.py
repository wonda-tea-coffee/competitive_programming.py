import re

S = input()

if re.fullmatch(r"\d{3}-\d{4}", S):
    print("Yes")
else:
    print("No")