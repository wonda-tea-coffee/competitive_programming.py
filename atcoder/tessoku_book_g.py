D = int(input())
N = int(input())
ratio = [0]*(D+2)
for _ in range(N):
    L, R = map(int, input().split())
    ratio[L] += 1
    ratio[R+1] -= 1
S = [0]
for r in ratio:
    S.append(S[-1] + r)

for i in range(1, D+1):
    print(S[i+1])
