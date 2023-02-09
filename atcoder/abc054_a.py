c = list(range(2, 14))
c.append(1)

A, B = map(int, input().split())
ai = c.index(A)
bi = c.index(B)
if ai < bi:
    print("Bob")
elif ai > bi:
    print("Alice")
else:
    print("Draw")
