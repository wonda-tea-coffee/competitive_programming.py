import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
Dic = [[] for _ in range(N+1)]
degree = [0]*(N+1)

for _ in range(M):
    a, b = map(int,input().split())
    Dic[a].append(b)
    degree[b] += 1

D = deque()
ans = [0]*(N+1)
cnt = 1
for i in range(1, N+1):
    if degree[i] == 0: D.append(i)

while D:
    n = D.popleft()
    ans[n] = cnt
    cnt += 1
    if D:
        print("No")
        exit()

    for num in Dic[n]:
        degree[num] -= 1
        if degree[num] == 0:
            D.append(num)

if cnt == N+1:
    print("Yes")
    print(*ans[1:])
else:
    print("No")
