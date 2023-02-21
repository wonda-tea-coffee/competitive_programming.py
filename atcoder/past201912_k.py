N = int(input())
C = [[] for _ in range(N)]
r = -1
for i in range(N):
    p = int(input())
    if p == -1:
        r = i
    else:
        C[p-1].append(i)

L = [-1] * N
R = [-1] * N
stk = [r]
t = -1
while stk:
    v = stk.pop()
    if v >= 0:
        t += 1
        L[v] = t
        stk.append(~v)
        for nv in C[v]:
            stk.append(nv)
    else:
        v = ~v
        R[v] = t

Q = int(input())
for _ in range(Q):
    a, b = map(lambda x: int(x)-1, input().split())
    if L[b] < L[a] <= R[b]:
        print("Yes")
    else:
        print("No")
