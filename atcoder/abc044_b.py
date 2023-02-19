from collections import defaultdict

d = defaultdict(lambda: 0)
w = input()
for i in range(len(w)):
    d[w[i]] += 1
for c in d:
    if d[c] % 2 == 1:
        print("No")
        exit()
print("Yes")
