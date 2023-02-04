h = {}
h["S"] = [False]*14
h["H"] = [False]*14
h["C"] = [False]*14
h["D"] = [False]*14

N = int(input())
for _ in range(N):
    s, n = input().split()
    h[s][int(n)] = True

for s in ["S", "H", "C", "D"]:
    for i in range(1, 14):
        if not h[s][i]:
            print(s, i)
