def tetrahedron(n):
    return n*(n+1)*(n+2)//6

def calc(a, dp):
    for ai in a:
        dp[ai] = 1
        for i in range(A+1):
            if i - ai >= 0:
                dp[i] = min(dp[i], dp[i - ai] + 1)

def solve(n):
    a = []
    b = []
    i = 1
    while tetrahedron(i) <= n:
        t = tetrahedron(i)
        a.append(t)
        if t % 2 == 1:
            b.append(t)
        i += 1

    calc(a, dp1)
    calc(b, dp2)

a = []
while True:
    ai = int(input())
    if ai == 0: break
    a.append(ai)

A = max(a)
dp1 = [A]*(A+1)
dp2 = [A]*(A+1)

solve(A)

for ai in a:
    print(dp1[ai], dp2[ai])
