N = int(input())
S = input()
E = [0]
W = [0]
cnte = 0
cntw = 0
for i in range(N):
    if S[i] == "E":
        cnte += 1
    else:
        cntw += 1
    E.append(cnte)
    W.append(cntw)

ans = 10**10
for i in range(N):
    # iより西の人に東を向かせて、iより東の人を西に向かせる
    ans = min(ans, W[i] + E[-1] - E[i+1])

print(ans)
