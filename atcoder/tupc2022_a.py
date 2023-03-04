N, K = map(int, input().split())
P = list(map(int, input().split()))

for i in range(N):
    if P[i] != i+1 and P[i] >= K:
        print("No")
        exit()

print("Yes")