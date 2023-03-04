import math

# a*b = nを満たす正整数a,bの個数を求める
def cnt(n):
    ans = 0
    for d in range(1, int(math.sqrt(n))+1):
        if n % d == 0:
            if d == n//d:
                ans += 1
            else:
                ans += 2
    return ans

N = int(input())

cnts = [0]*N
for i in range(1, N):
    cnts[i] = cnt(i)

ans = 0
for x in range(1, N):
    y = N-x
    ans += cnts[x] * cnts[y]

print(ans)
