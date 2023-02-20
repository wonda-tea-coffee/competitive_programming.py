S = input()
ans = 0

mae = "Z"
buf = ""
for i in range(len(S)):
    buf += S[i]
    if buf == mae:
        pass
    else:
        ans += 1
        # print(buf, ans)
        mae = buf
        buf = ""

print(max(ans, 1))