N = int(input())
S = input()

h = {}
for i in range(N):
    if S[i] in h:
        h[S[i]].append(i)
    else:
        h[S[i]] = [i]

ans = 0

for i in range(1000):
    s = "%03d" % i
    t = -1
    res = True
    for j in range(3):
        if not s[j] in h:
            res = False
            break

        res2 = False

        for k in h[s[j]]:
            if t == -1 or t < k:
                t = k
                res2 = True
                break

        if not res2:
            res = False
            break

    if res:
        ans += 1

print(ans)
