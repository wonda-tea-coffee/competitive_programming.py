S = input()
N = len(S)
ans = 0

for i in range(N):
    if S[i] == "U":
        # 上の階には1回で行ける
        ans += N-i-1
        # 下の階には2回で行ける
        ans += 2*i
    else:
        # 上の階には2回で行ける
        ans += 2*(N-i-1)
        # 下の階には1回で行ける
        ans += i

print(ans)
