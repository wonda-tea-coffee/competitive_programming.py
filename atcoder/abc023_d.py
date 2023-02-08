import sys
input = lambda: sys.stdin.readline().rstrip()

# Hi + Si * N <= X
# Si * N <= X - Hi
# N <= (X - Hi)/Si
def check(X):
    A = [0] * N
    for i in range(N):
        if X < H[i]: return False

        A[i] = ((X - H[i])//S[i], H[i], S[i])
    A.sort()
    mx = 0

    for i in range(N):
        t, h, s = A[i]
        if i > t: return False

        mx = max(mx, h + s * i)
        if mx > X: return False

    return True

N = int(input())
H = [0] * N
S = [0] * N
M = 10**9
for i in range(N):
    h, s = map(int, input().split())
    H[i] = h
    S[i] = s

ng = 0
ok = M*N
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
