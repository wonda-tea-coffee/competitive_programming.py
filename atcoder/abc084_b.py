import re

A, B = map(int, input().split())
S = input()
if re.fullmatch(r"[0-9]{" + str(A) + r"}\-[0-9]{" + str(B) + r"}", S):
    print("Yes")
else:
    print("No")