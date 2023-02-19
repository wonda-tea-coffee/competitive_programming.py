N = int(input())
mae = input()
seen = set([mae])
res = True
for i in range(N-1):
    w = input()
    if mae[-1] == w[0] and not w in seen:
        pass
    else:
        res = False
    mae = w
    seen.add(w)

if res:
    print("Yes")
else:
    print("No")
