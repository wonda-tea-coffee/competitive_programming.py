X = int(input())
d = X % 100
s = 0
i = 5
while i >= 1 and d > 0:
    s += d // i
    d %= i
    i -= 1
# print(s)
if 100*s <= X:
    print(1)
else:
    print(0)
