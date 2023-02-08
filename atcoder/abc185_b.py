N, M, T = map(int, input().split())
res = True
t = 0
n = N
for i in range(M):
    # print("t = ", t, "n = ", n)
    a, b = map(int, input().split())
    if not res: continue

    n -= a - t
    t = a
    # print("t = ", t, "N = ", N)
    if n <= 0:
        res = False
        continue

    n = min(n + b - a, N)
    t = b
    # print("t = ", t, "n = ", n)

if res and n > T - t:
    print("Yes")
else:
    print("No")
