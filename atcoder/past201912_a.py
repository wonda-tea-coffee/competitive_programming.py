import re

S = input()

if re.search('^\d+$', S):
    print(int(S)*2)
else:
    print("error")
