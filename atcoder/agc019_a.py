Q, H, S, D = map(lambda x: int(x)*4, input().split())
X = sorted([(Q/1, 1, Q), (H/2, 2, H), (S/4, 4, S), (D/8, 8, D)])
N = int(input())*4
ans = 0
for v, i, c in X:
    # print(v, i, c)
    ans += (N // i) * c
    N %= i
print(ans//4)
