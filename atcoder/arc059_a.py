import math

N = int(input())
a = list(map(int, input().split()))

ans1 = 0
ans2 = 0
suma = sum(a)
avg1 = math.ceil(suma/N)
avg2 = suma//N
for i in range(N):
    ans1 += (a[i] - avg1)**2
    ans2 += (a[i] - avg2)**2
print(min(ans1, ans2))
