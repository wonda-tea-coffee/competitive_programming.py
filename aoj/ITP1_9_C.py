n = int(input())
s1 = 0
s2 = 0
for _ in range(n):
    w0, w1 = input().split()
    if w0 > w1:
        s1 += 3
    elif w0 < w1:
        s2 += 3
    else:
        s1 += 1
        s2 += 1

print(s1, s2)