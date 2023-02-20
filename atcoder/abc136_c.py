N = int(input())
H = list(map(int, input().split()))
M = 0
for i in range(N):
    if M-H[i] >= 2:
        print("No")
        exit()
    M = max(M, H[i])

print("Yes")