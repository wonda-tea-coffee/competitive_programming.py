import math

def solve(n, d, k):
    d %= n
    k -= 1
    if d == 0: return k

    g = math.gcd(n, d)
    lcm = n * d // g
    s = lcm // d
    # print("gcd(%d, %d) = %d" % (n, d, g))

    if g > 1:
        return (d * k % n + k // s) % n
    else:
        return d * k % n

T = int(input())
for _ in range(T):
    N, D, K = map(int, input().split())
    print(solve(N, D, K))
