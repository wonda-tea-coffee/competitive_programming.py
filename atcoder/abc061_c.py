import heapq

N, K = map(int, input().split())
Q = [tuple(map(int, input().split())) for _ in range(N)]
heapq.heapify(Q)

s = 0
for i in range(N):
    a, b = heapq.heappop(Q)
    s += b
    if s >= K:
        print(a)
        exit()
