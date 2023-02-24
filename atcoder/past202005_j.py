import bisect

N, M = map(int, input().split())
a = list(map(int, input().split()))
ans = [-1]*M
# child[i]: 子供iが直近で食べた寿司
child = [10**10]*N

for i in range(M):
    br = bisect.bisect_right(child, -a[i])
    if br >= N: continue
    ans[i] = br+1
    child[br] = -a[i]

for i in range(M):
    print(ans[i])
