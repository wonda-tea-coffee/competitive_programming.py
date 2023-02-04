import sys

S = input()
for i in range(3):
    if S.count(S[i]) == 1:
        print(S[i])
        sys.exit(0)

print(-1)
