A, B, K = map(int, input().split())
s = set()
i1 = A
c1 = 0
while i1 <= B and c1 < K:
    s.add(i1)
    i1 += 1
    c1 += 1
i2 = B
c2 = 0
while i2 >= A and c2 < K:
    s.add(i2)
    i2 -= 1
    c2 += 1

print("\n".join(list(map(lambda x: str(x), sorted(list(s))))))
