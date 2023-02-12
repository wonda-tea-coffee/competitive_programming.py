def s(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

N = int(input())
ans = 10**100
for a in range(1, N//2 + 1):
    ans = min(ans, s(a) + s(N-a))
print(ans)