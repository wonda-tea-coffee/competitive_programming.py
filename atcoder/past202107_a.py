S = list(map(int, list(input())))

a = 0
for i in range(0, len(S)-1, 2):
    a += S[i]*3

b = 0
for i in range(1, len(S)-1, 2):
    b += S[i]

if (a + b) % 10 == S[-1]:
    print("Yes")
else:
    print("No")
