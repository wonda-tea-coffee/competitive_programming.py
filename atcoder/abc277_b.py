N = int(input())
c1 = True
c2 = True
s = set()
for _ in range(N):
    si = input()
    c1 &= si[0] in {"H", "D", "C", "S"}
    c2 &= si[1] in {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}
    s.add(si)

if c1 and c2 and len(s) == N:
    print("Yes")
else:
    print("No")