S = list(input())

for i in range(len(S)):
    if "a" <= S[i] <= "z" or "A" <= S[i] <= "Z":
        osi = ord(S[i])

        if osi >= 97:
            S[i] = chr(osi - 32)
        else:
            S[i] = chr(osi + 32)

print("".join(S))