N = int(input())
Q = []
for _ in range(N):
    a, b = map(int, input().split())
    Q.append((b, a))
Q.sort()

t = 0
for b, a in Q:
    t += a
    if t <= b:
        pass
    else:
        exit(print("No"))

print("Yes")
