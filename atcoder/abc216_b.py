N = int(input())
s = set([tuple(input().split()) for _ in range(N)])

if len(s) < N:
    print("Yes")
else:
    print("No")