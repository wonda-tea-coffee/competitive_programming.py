import sys

S = input()
T = input()
ls = len(S)
for i in range(ls):
    if S[i] != T[i]:
        print(i+1)
        sys.exit(0)

print(ls+1)