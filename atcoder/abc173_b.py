from collections import defaultdict

N = int(input())
d = defaultdict(lambda: 0)
for _ in range(N):
    d[input()] += 1

for t in ["AC", "WA", "TLE", "RE"]:
    print("%s x %d" % (t, d[t]))
