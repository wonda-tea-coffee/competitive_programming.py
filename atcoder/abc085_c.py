import sys

N, Y = map(int, input().split())
M = Y//1000 - N

b = 0
while M - 4*b >= 0:
    if (M - 4*b) % 9 == 0:
        a = (M - 4*b) // 9
        if a + b <= N:
            print(a, b, N-a-b)
            sys.exit(0)

    b += 1

print("-1 -1 -1")