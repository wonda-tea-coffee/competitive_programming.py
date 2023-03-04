N = int(input())
A = list(map(int, input().split()))
even = []
odd = []
for ai in A:
    if ai % 2 == 0:
        even.append(ai)
    else:
        odd.append(ai)

ans = -1
if len(even) > 1:
    even.sort()
    ans = even[-1] + even[-2]

if len(odd) > 1:
    odd.sort()
    ans = max(ans, odd[-1] + odd[-2])

print(ans)