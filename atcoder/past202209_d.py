N, M = map(int, input().split())
edges = [set() for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    if 1 <= u <= N and 1 <= v <= N and u != v and not v in edges[u]:
        edges[u].add(v)
        edges[v].add(u)
    else:
        print("No")
        exit()

print("Yes")
