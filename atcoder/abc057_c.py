def F(a, b):
    la = len(str(a))
    lb = len(str(b))
    return max(la, lb)

N = int(input())
ans = 10**100

i = 1
while i*i <= N:
    if N % i == 0:
        ans = min(ans, F(i, N//i))
    i += 1

print(ans)
