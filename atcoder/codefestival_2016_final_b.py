N = int(input())

a = 1
while a*(a+1)//2 < N:
    a += 1

ans = []
s = N
for i in range(a, 0, -1):
    if s - i >= 0:
        ans.append(i)
        s -= i

print("\n".join(map(str, reversed(ans))))