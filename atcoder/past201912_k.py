import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
E = [[] for _ in range(N)]
root = -1
for i in range(N):
    p = int(input())
    if p == -1:
        root = i
    else:
        E[i].append(p-1)
        E[p-1].append(i)

L = [-1] * N
R = [-1] * N

idx = 0
def euler_tour(i, pa=-1):
    global idx

    L[i] = idx
    idx += 1
    for to in E[i]:
        if to == pa: continue
        euler_tour(to, i)
    R[i] = idx

euler_tour(root)

# print("L:", L)
# print("R:", R)

Q = int(input())
for _ in range(Q):
    a, b = map(lambda x: int(x)-1, input().split())
    if L[b] <= L[a] and R[a] <= R[b]:
        print("Yes")
    else:
        print("No")
