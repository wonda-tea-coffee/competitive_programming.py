N = int(input())
a = list(map(int, input().split()))
target = 1
for ai in a:
    if ai == target:
        target += 1

if target == 1:
    print(-1)
else:
    print(N - (target - 1))