import random

N = int(input())
S = input()

if len(S) <= 2 or len(set(S)) == 1:
    print("None")
else:
    T = list(S)
    while "".join(T) == S or "".join(T) == "".join(reversed(S)):
        random.shuffle(T)
    print("".join(T))
