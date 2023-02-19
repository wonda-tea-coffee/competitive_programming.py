N, K = map(int, input().split())
S = input()
res = [False]*N
cnt = 0
for i in range(N):
    if S[i] == "o":
        cnt += 1
        if cnt <= K:
            res[i] = True
T = ""
for i in range(N):
    if res[i]:
        T += "o"
    else:
        T += "x"
print(T)