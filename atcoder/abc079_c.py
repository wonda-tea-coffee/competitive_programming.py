S = list(map(int, list(input())))
for bit in range(1<<3):
    c = S[0]
    for i in range(3):
        c += S[i+1] * (-1)**((bit>>i)&1)
    if c != 7: continue

    print(S[0], end="")
    for i in range(3):
        if (bit>>i)&1:
            print("-", end="")
        else:
            print("+", end="")
        print(S[i+1], end="")
    print("=7")
    break