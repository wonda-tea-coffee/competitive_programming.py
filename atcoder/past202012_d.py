N = int(input())
S = []
for _ in range(N):
    s = input()

    i = 0
    z = 0
    while i < len(s) and s[i] == "0":
        z += 1
        i += 1

    S.append((int(s), -z, s))

S.sort()
for si in S:
    print(si[2])
