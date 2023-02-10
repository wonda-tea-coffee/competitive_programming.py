N = int(input())
h = {}
for i in range(N):
    l = list(map(int, list(input())))
    for j in range(N):
        if l[j] in h:
            h[l[j]].append((i, j))
        else:
            h[l[j]] = [(i, j)]

# N桁選ぶ
for i in range(N):
    # 大きい方から優先的に
    for j in range(9, 0, -1):
        if not j in h: continue
        if len(h[j]) == 0: continue
        
