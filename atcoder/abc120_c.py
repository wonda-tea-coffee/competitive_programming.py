S = input()
c = S.count("1")
print(min(c, len(S)-c)*2)
