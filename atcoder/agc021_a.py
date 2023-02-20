# c + 9(K - 1)
N = input()
iN = int(N)
K = len(N)
c = int(N[0])
ans = c + 9*(K - 1)
if iN < 10:
    print(N)
elif set(N[1:])=={"9"}:
    print(ans)
else:
    print(ans-1)
