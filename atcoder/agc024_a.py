A, B, C, K = map(int, input().split())
r = (A-B)*(-1)**K
if abs(r) > 10**18:
    print("Unfair")
else:
    print(r)