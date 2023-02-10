S, T = input().split()

if S[0] == "B":
    s = -int(S[1])
else:
    s = int(S[0])

if T[0] == "B":
    t = -int(T[1])
else:
    t = int(T[0])

if (s > 0 and t > 0) or (s < 0 and t < 0):
    print(abs(s - t))
else:
    print(abs(s) + abs(t) - 1)
