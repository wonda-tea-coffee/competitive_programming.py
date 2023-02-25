s = [input() for _ in range(3)]
l = [len(s[i]) for i in range(3)]
i = [0] * 3
t = 0
while True:
    if i[t] == l[t]:
        print(chr(t+65))
        exit()

    c = s[t][i[t]]
    i[t] += 1
    t = ord(c)-97
