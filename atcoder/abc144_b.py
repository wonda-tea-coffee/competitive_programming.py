s = set()
for i in range(1, 10):
    for j in range(1, 10):
        s.add(i*j)

N = int(input())
if N in s:
    print("Yes")
else:
    print("No")
