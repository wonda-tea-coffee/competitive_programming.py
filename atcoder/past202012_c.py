c = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
N = int(input())

r = []
while True:
    r.append(c[N % 36])
    N //= 36
    if N == 0: break

print("".join(reversed(r)))
