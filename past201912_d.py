N = int(input())
h = {}

bad = None
t = None
for i in range(N):
    a = int(input())
    if a in h:
        h[a] += 1
        if h[a] > 1:
            t = a
    else:
        h[a] = 1

diff = set(range(1, N+1)) - set(h)
if len(diff) > 0:
    print(t, list(diff)[0])
else:
    print("Correct")
