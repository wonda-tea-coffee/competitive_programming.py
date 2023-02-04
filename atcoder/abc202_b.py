S = input()
h = {}
h["0"] = "0"
h["1"] = "1"
h["6"] = "9"
h["8"] = "8"
h["9"] = "6"
for i in range(len(S)-1, -1, -1):
    print(h[S[i]], end="")
print()
