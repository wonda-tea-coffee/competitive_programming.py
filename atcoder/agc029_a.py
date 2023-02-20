S = input()

if not "B" in S:
    print(0)
    exit()

ans = 0
cnt = 0
for i in range(len(S)):
    if S[i] == "W":
        ans += i-cnt
        cnt += 1
print(ans)
