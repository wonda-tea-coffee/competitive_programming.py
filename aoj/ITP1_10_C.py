import math

while True:
    n = int(input())
    if n == 0: break
    s = list(map(int, input().split()))
    m = sum(s) / n

    t = 0
    for si in s:
        t += (si - m) ** 2
    a = math.sqrt(t / n)
    print(a)
