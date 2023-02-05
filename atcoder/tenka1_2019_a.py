A, B, C = map(int, input().split())

if C in range(min(A, B), max(A, B)):
    print("Yes")
else:
    print("No")