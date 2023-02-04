a, b = map(int, input().split())
s = str(a)*b
t = str(b)*a
if s < t:
    print(s)
else:
    print(t)
