import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    v = bisect.bisect_left(A, B[i]) * (N - bisect.bisect_right(C, B[i]))
    # print(B[i], v)
    ans += v

print(ans)
