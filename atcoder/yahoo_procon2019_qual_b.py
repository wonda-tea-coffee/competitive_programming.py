from collections import defaultdict

d = defaultdict(lambda: 0)
for _ in range(3):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1

for i in range(1, 5):
    if d[i] == 3:
        print("NO")
        exit()

print("YES")
