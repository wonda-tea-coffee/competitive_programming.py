while True:
    S = input()
    if S == "-": break

    m = int(input())
    for _ in range(m):
        h = int(input())
        S = S[h:] + S[:h]
    print(S)