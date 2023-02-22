s = input()
ans = []
for si in s:
    if si == "B":
        if ans:
            ans.pop()
    else:
        ans.append(si)

print("".join(ans))