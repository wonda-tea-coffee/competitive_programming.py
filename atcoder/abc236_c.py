N, M = map(int, input().split())
S = input().split()
T = set(input().split())
for si in S:
    if si in T:
        print("Yes")
    else:
        print("No")