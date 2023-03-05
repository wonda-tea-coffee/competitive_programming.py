N = int(input())
P = list(map(int, input().split()))
i = N-2
t = [P[-1]]
while i >= 0 and t[-1] > P[i]:
    t.append(P[i])
    i -= 1

a = P[i]
t.append(a)
t.sort(reverse=True)
b = t[t.index(a)+1]
P[i] = b
t.remove(b)
for j in range(len(t)):
    P[i+1+j] = t[j]

print(*P)
