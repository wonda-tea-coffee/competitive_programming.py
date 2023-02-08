S = input()
l = []
for _ in range(len(S)):
    T = S[-1] + S[:-1]
    l.append(T)
    S = T

l.sort()
print(l[0])
print(l[-1])
