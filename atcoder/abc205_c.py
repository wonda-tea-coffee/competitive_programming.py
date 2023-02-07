A, B, C = map(int, input().split())

if A < 0 and C % 2 == 0: A = -A
if B < 0 and C % 2 == 0: B = -B

if A >= 0 and B >= 0:
    r = A - B
elif A >= 0 and B < 0:
    r = 1
elif A < 0 and B >= 0:
    r = -1
else:
    r = A - B
# print(A, B, r)
if r > 0:
    print(">")
elif r < 0:
    print("<")
else:
    print("=")
