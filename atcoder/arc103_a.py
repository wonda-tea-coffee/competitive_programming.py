from collections import Counter

n = int(input())
v = list(map(int, input().split()))
c1 = Counter(v[::2]).most_common() + [(0, 0)]
c2 = Counter(v[1::2]).most_common() + [(0, 0)]

if c1[0][0] == c2[0][0]:
    print(min(n - c1[0][1] - c2[1][1], n - c1[1][1] - c2[0][1]))
else:
    print(n - c1[0][1] - c2[0][1])