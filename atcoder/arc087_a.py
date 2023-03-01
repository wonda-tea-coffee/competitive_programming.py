from collections import Counter

N = int(input())
a = list(map(int, input().split()))

c = Counter(a)
ans = 0
for ci in c:
    if ci > c[ci]:
        ans += c[ci]
    else:
        ans += c[ci] - ci
print(ans)
