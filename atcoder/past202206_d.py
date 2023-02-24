from collections import deque, defaultdict

N = int(input())
d = defaultdict(list)
for _ in range(N):
    a, b = input().split()
    d[a].append(b)
    d[b].append(a)
S = input()
T = input()

def bfs(s, t):
    Q = deque([s])
    done = set([s])

    while Q:
        cur = Q.popleft()
        if cur == t: return True

        for to in d[cur]:
            if to in done: continue
            Q.append(to)
            done.add(to)

    return False

if all(bfs(S[i], T[i]) for i in range(len(S))):
    print("Yes")
else:
    print("No")
