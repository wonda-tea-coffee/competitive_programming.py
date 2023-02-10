N = int(input())
a = []
for i in range(N):
    s, p = input().split()
    a.append((s, -int(p), i+1))
a.sort()

for i in range(N):
    print(a[i][2])