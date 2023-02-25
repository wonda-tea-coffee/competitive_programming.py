N, Q = map(int, input().split())
S = input()
D = [0, 0]
for i in range(1, N):
    d = D[-1]
    if S[i-1] + S[i] == "AC":
        d += 1
    D.append(d)

for _ in range(Q):
    l, r = map(int, input().split())
    print(D[r] - D[l])
