N = int(input())
S = input()
T = list(S)
t = ["axa", "ixi", "uxu", "exe", "oxo"]

i = 2
while i < N:
    res = False
    for ti in t:
        if ti == S[i-2:i+1]:
            T[i-2] = T[i-1] = T[i] = "."
            res = True
            break
    if res:
        i += 3
    else:
        i += 1
print("".join(T))