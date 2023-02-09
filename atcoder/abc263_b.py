N = int(input())
P = [-1, -1] + list(map(int, input().split()))

s = N
ans = 0
while s != 1:
    # print("%d -> %d" % (s, P[s]))
    s = P[s]
    ans += 1

print(ans)