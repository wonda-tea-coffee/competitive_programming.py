S = input()
N = len(S)
i = 0
ans = 0
while i < N:
    l = i
    lc = 0
    while l < N and S[l] == "<":
        l += 1
        lc += 1

    r = l
    rc = 0
    while r < N and S[r] == ">":
        r += 1
        rc += 1

    if lc >= rc:
        ans += lc*(lc+1)//2
        ans += (rc-1)*rc//2
    else:
        ans += (lc-1)*lc//2
        ans += rc*(rc+1)//2

    # print(l, lc, r, rc)
    i = r

print(ans)
