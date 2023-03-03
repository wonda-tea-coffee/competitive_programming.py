N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [a-b for a, b in zip(A, B)]
neg = list(filter(lambda x: x < 0, C))
ans = len(neg)
need = -sum(neg)
pos = sorted(list(filter(lambda x: x > 0, C)))
for p in pos[::-1]:
    if need > 0:
        need -= p
        ans += 1
    else:
        break

if need > 0:
    print(-1)
else:
    print(ans)
