S = list(input())

if len(S) % 2 == 1:
    S.pop()
else:
    S.pop()
    S.pop()

while S:
    m = len(S)//2
    if S[:m] == S[m:]:
        print(m*2)
        exit()
    S.pop()
    S.pop()
