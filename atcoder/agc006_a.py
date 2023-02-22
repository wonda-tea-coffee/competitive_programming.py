N = int(input())
S = input()
T = input()
for i in range(N):
    if S[i:] == T[:N-i]:
        print(N+i)
        exit()

print(2*N)