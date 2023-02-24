import sys
input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n):
        self.n = n
        # 正の数の場合は親のインデックス
        # 負の数の場合は木のサイズ
        self.parent_or_size = [-1] * n
        self.group = []
        for i in range(n):
            self.group.append([i])

    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)
        if x == y: return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.group[x] += self.group[y]
        self.group[y] = []
        self.parent_or_size[y] = x

        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        if self.parent_or_size[a] < 0: return a

        # 効率化のための根の付け替え
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def connected_component(self, a):
        return sorted(self.group[self.leader(a)])


N, Q = map(int, input().split())
uf = UnionFind(N+1)
res = []
for _ in range(Q):
    t, *q = map(int, input().split())

    if t == 1:
        u, v = q
        if not uf.same(u, v):
            uf.merge(u, v)
    else:
        u = q[0]
        print(*uf.connected_component(u))

# print("\n".join(map(str, res)))
