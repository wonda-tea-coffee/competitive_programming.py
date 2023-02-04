S = input()
ans = True
for i in range(len(S)):
    if i % 2 == 0 and "a" <= S[i] <= "z" or i % 2 == 1 and "A" <= S[i] <= "Z":
        pass
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
