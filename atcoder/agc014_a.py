A, B, C = map(int, input().split())
seen = set([(A, B, C)])
i = 0
while True:
    if A%2 == 1 or B%2 == 1 or C%2 == 1:
        print(i)
        exit()

    A, B, C = (B+C)//2, (A+C)//2, (A+B)//2
    if (A, B, C) in seen:
        print(-1)
        exit()

    i += 1
