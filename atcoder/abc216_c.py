s = list("{0:b}".format(int(input())))

ans = []
while s != ["0"]:
    if s[-1] == "0":
        s.pop()
        ans.append("B")
    else:
        s[-1] = "0"
        ans.append("A")

print("".join(ans[::-1]))
