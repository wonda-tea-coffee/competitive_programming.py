a, b, c, d = -1, -1, -1, -1
for i in range(1, 11):
    s = input()
    if s.count("#") > 0:
        if a == -1:
            a = i
        b = i
    for j in range(10):
        if s[j] == "#":
            if c == -1:
                c = j+1
            d = j+1

print(a, b)
print(c, d)