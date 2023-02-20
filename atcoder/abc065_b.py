N = int(input())
x = 0
a = [int(input())-1 for _ in range(N)]
ans = 0
seen = set()
while x != 1:
    if x in seen:
        print(-1)
        exit()
    else:
        seen.add(x)
    x = a[x]
    ans += 1
print(ans)
