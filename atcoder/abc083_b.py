def s(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

ans = 0
N, A, B = map(int, input().split())

for i in range(N+1):
    if A <= s(i) <= B:
        ans += i

print(ans)