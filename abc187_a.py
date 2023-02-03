def s(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

A, B = map(int, input().split())
if s(A) < s(B):
    print(s(B))
else:
    print(s(A))
