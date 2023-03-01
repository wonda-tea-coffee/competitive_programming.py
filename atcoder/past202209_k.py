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

def build_union_find_tree(edges):
    uf = UnionFind(N+1)
    for i in range(1, N+1):
        for j in edges[i]:
            if not uf.same(i, j):
                uf.merge(i, j)
    return uf

N, M = map(int, input().split())
edges = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

Q = int(input())
query = []
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        edges[x].add(y)
        edges[y].add(x)
    elif t == 2:
        edges[x].remove(y)
        edges[y].remove(x)
    query.append((t, x, y))

ans = []

uf = build_union_find_tree(edges)
for t, x, y in query[::-1]:
    if t == 1:
        edges[x].remove(y)
        edges[y].remove(x)
        uf = build_union_find_tree(edges)
    elif t == 2:
        edges[x].add(y)
        edges[y].add(x)
        if not uf.same(x, y):
            uf.merge(x, y)
    else:
        ans.append("Yes" if uf.same(x, y) else "No")

for a in ans[::-1]:
    print(a)
