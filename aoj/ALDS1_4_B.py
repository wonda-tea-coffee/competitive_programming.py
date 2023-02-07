import bisect

n = int(input())
S = sorted(list(map(int, input().split())))
q = int(input())
T = sorted(list(map(int, input().split())))

ans = 0
for ti in T:
    i = bisect.bisect_right(S, ti)
    if S[i-1] == ti: ans +=1

print(ans)
