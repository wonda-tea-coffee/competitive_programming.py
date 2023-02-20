S = input()
K = int(input())
c = 0
while c < len(S) and S[c] == "1":
    c += 1

if K <= c:
    print(1)
else:
    print(S[c])
