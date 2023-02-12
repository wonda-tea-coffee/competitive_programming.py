from collections import defaultdict

H, W, K = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(map(int, list(input()))))

ans = 0
for n in range(1, min(H, W)+1):
    res = False
    # print("n = ", n)
    for i in range(H-n+1):
        for j in range(W-n+1):
            # print("  i = %d, j = %d" % (i, j))
            d = defaultdict(lambda: 0)
            for k in range(n):
                for l in range(n):
                    d[S[i+k][j+l]] += 1
            e = []
            for key in d:
                e.append((-d[key], key))
            e.sort()

            c = 0
            for ei in range(1, len(e)):
                c -= e[ei][0]

            if c <= K:
                res = True
                break

        if res: break
    if res:
        ans = n

print(ans)
