S = input()
T = input()
if len(S)+1 == len(T) and S == T[:len(S)]:
    print("Yes")
else:
    print("No")