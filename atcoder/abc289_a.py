s = input()
for i in range(len(s)):
    if s[i] == "0":
        print("1", end="")
    else:
        print("0", end="")
print()