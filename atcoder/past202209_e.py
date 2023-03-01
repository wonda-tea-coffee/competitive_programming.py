R, N, M, L = map(int, input().split())
s = list(map(int, input().split()))
f = [False]*L
sl = 0
for r in range(1, R+1):
    stick = N
    sr = sl + M
    # print("Round", r)
    for si in range(sl, sr):
        if si >= L or s[si] > stick:
            print("No")
            exit()
        else:
            stick -= s[si]
            f[si] = True
            # print("  +", s[si])
            if stick == 0:
                sl = si+1
                break
    if stick > 0:
        sl = sr

if all(f):
	print("Yes")
else:
    print("No")
