import bisect

N = int(input())
d = sorted(list(map(int, input().split())))
k = 0
ans = 0
while True:
    # k未満の数がいくつあるか
    abc = bisect.bisect_left(d, k)
    if abc > N//2:
        break
    elif abc == N//2:
        ans += 1
    k += 1

print(ans)
