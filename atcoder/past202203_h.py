from collections import deque
import sys
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
E = [[] for _ in range(N)]
uf = UnionFind(N)

for _ in range(Q):
    t, *q = map(lambda x: int(x)-1, input().split())
    if t == 0:
        u, v = q
        if not uf.same(u, v):
            uf.merge(u, v)
            E[u].append(v)
            E[v].append(u)
    else:
        visited = [False]*N
        res = []
        Q = deque([(q[0], -1)])
        while Q:
            cur, pre = Q.popleft()
            res.append(cur)

            for to in E[cur]:
                if to == pre: continue
                Q.append((to, cur))
        print(*map(lambda x: x+1, sorted(res)))
