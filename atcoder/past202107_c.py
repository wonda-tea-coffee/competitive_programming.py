S = input()
L, R = map(int, input().split())

if (len(S) == 1 or len(S) != 1 and S[0] != "0") and L <= int(S) <= R:
    print("Yes")
else:
    print("No")