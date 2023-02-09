N = int(input())
S = input()
for i in range(1, N):
    l = 0
    j = 0
    while j + i < N and S[j] != S[j + i]:
        l += 1
        j += 1

    print(l)
