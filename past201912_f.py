S = input()

cnt = 0
buf = ""
words = []
for i in range(len(S)):
    buf += S[i]
    if ord(S[i]) <= 90:
        cnt += 1
        if cnt == 2:
            words.append(buf)
            buf = ""
            cnt = 0

sorted_words = sorted(words, key=lambda s: s.lower())
# print(words)
# print(sorted_words)
print(''.join(sorted_words))
