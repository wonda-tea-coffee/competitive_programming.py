N = int(input())
S = list(input())
is_enclose = False
for i in range(N):
    if S[i] == '"':
        is_enclose = not is_enclose
    elif S[i] == "," and not is_enclose:
        S[i] = "."
print("".join(S))
