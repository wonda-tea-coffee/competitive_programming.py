S = input()
h = {}

for i in range(1, len(S)):
    t = S[i-1] + S[i]
    if t in h:
        h[t] += 1
    else:
        h[t] = 1

words = []
cnt = 0
for hi in h:
    if h[hi] > cnt:
        words = [hi]
        cnt = h[hi]
    elif h[hi] == cnt:
        words.append(hi)

words.sort()
print(words[0])
