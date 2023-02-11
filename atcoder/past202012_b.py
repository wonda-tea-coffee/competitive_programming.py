N = int(input())
S = input()
T = []

for i in range(N):
    while S[i] in T:
        T.remove(S[i])
    T.append(S[i])

print("".join(T))
