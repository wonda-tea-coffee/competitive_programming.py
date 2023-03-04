from collections import defaultdict, deque

N = int(input())
E = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    E[A].append(B)
    E[B].append(A)

que = deque([1])
ans = 1
visited = set([1])
while que:
    cur = que.popleft()
    ans = max(ans, cur)
    for to in E[cur]:
        if to in visited: continue
        visited.add(to)
        que.append(to)

print(ans)
