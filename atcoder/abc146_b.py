import string

N = int(input())
S = input()
A = list(string.ascii_uppercase)
ans = ""
for i in range(len(S)):
    j = A.index(S[i])
    ans += A[(j + N) % 26]

print(ans)