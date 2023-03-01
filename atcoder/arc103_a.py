from collections import Counter

n = int(input())
v = list(map(int, input().split()))

r = []

c1 = Counter(v[::2])
q1 = []
for ci1 in c1:
    q1.append((c1[ci1], ci1))
q1.append((0, 0))
q1.sort(reverse=True)

c2 = Counter(v[1::2])
q2 = []
for ci2 in c2:
    q2.append((c2[ci2], ci2))
q2.append((0, 0))
q2.sort(reverse=True)

if q1[0][1] == q2[0][1]:
    print(min(n//2 - q1[0][0] + n//2 - q2[1][0], n//2 - q1[1][0] + n//2 - q2[0][0]))
else:
    print(n//2 - q1[0][0] + n//2 - q2[0][0])
