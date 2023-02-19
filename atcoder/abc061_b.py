N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    E[a].append(b)
    E[b].append(a)
for i in range(N):
    print(len(E[i]))
