import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n):
        self.n = n
        # 正の数の場合は親のインデックス
        # 負の数の場合は木のサイズ
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)
        if x == y: return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        if self.parent_or_size[a] < 0: return a

        # 効率化のための根の付け替え
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

N, Q = map(int, input().split())
uf = UnionFind(N)
G = [[] for _ in range(N)]
for _ in range(Q):
    query = tuple(map(lambda x: int(x)-1, input().split()))

    if query[0] == 0:
        t, u, v = query
        if not uf.same(u, v):
            uf.merge(u, v)
            G[u].append(v)
            G[v].append(u)
    else:
        t, u = query
        que = deque([(u, -1)])
        res = [u]
        while que:
            cur, pre = que.popleft()
            for gi in G[cur]:
                if gi == pre: continue
                que.append((gi, cur))
                res.append(gi)
        print(*sorted(map(lambda x: x+1, res)))
