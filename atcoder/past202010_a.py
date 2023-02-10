a = list(map(int, input().split()))
a[0] = (a[0], "A")
a[1] = (a[1], "B")
a[2] = (a[2], "C")

a.sort()
print(a[1][1])
