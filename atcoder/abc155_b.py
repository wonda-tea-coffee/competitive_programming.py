N = int(input())
A = list(map(int, input().split()))

res = True
for ai in A:
    if ai % 2 > 0: continue

    if ai % 3 > 0 and ai % 5 > 0:
        res = False
        break

if res:
    print("APPROVED")
else:
    print("DENIED")