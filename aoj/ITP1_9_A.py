import sys

W = input()
S = sys.stdin.read()

T = []
for line in S.split("\n"):
    for w in line.split():
        T.append(w.lower())

print(T.count(W))
