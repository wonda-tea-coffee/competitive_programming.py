import bisect

N = int(input())
A = list(map(int, input().split()))
B = sorted(set(A))

ans = []
for ai in A:
    i = bisect.bisect_left(B, ai)
    ans.append(i+1)
print(*ans)
