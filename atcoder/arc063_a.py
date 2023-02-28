S = input()
N = len(S)
ans = 0
i = 0
while i < N:
    j = i
    ans += 1
    while j < N and S[j] == S[i]:
        j += 1
    i = j
print(ans-1)