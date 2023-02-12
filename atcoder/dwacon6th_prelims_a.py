N = int(input())
S = []
T = []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
X = input()

ans = 0
xi = S.index(X)
print(sum(T[xi+1:]))