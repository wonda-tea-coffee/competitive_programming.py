N, M = map(int, input().split())
AC = [0]*N
WA = [0]*N
for _ in range(M):
    p, s = input().split()
    p = int(p)-1
    if s == "AC":
        AC[p] += 1
    else:
        if AC[p] == 0:
            WA[p] += 1

ac = 0
wa = 0
for i in range(N):
    if AC[i] > 0:
        ac += 1
        wa += WA[i]
print(ac, wa)
