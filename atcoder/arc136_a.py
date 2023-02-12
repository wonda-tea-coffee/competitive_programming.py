# Cは無視
# BA -> BBB -> AB
# BB -> A
N = int(input())
S = list(input())

ans = []
i = 0
while i < N:
    if S[i] != "B":
        ans.append(S[i])
        i += 1
        continue

    if i == N-1:
        ans.append(S[i])
        break

    if S[i+1] == "A":
        ans.append("A")
        S[i+1] = "B"
        i += 1
    elif S[i+1] == "B":
        ans.append("A")
        i += 2
    else:
        ans.append("B")
        i += 1

print("".join(ans))
