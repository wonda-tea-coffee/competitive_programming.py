import string
from collections import deque, defaultdict

Q = int(input())
S = deque()
for _ in range(Q):
    query = input().split()

    if len(query) == 3:
        _, c, x = query
        S.append((c, int(x)))
    else:
        _, d = query
        d = int(d)
        cnt = defaultdict(int)
        while S and d > 0:
            c, x = S.popleft()
            if x <= d:
                cnt[c] += x
                d -= x
            else:
                cnt[c] += d
                S.appendleft((c, x-d))
                d = 0
        ans = 0
        for a in string.ascii_lowercase:
            ans += cnt[a]**2
        print(ans)
