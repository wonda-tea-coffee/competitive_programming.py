from string import ascii_lowercase
alphabets = input()
t = str.maketrans(alphabets, ascii_lowercase)
N = int(input())
S = [input() for _ in range(N)]
print(*sorted(S, key=lambda s: s.translate(t)), sep="\n")
