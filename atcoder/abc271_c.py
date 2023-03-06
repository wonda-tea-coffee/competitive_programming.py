from collections import deque

N = int(input())
a = list(map(int, input().split()))

ans = 0
stock = 0
memo = set()
for ai in a:
    if ai in memo: stock += 1
    memo.add(ai)
a = deque(sorted(list(set(a))))

while a:
    if a[0] == ans+1:
        ans += 1
        a.popleft()
    elif stock >= 2:
        ans += 1
        stock -= 2
    else:
        while a and stock < 2:
            stock += 1
            a.pop()
        if stock < 2:
            break

print(ans + stock//2)
