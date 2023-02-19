N = int(input())
T = list(map(int, input().split()))
sumt = sum(T)
M = int(input())
for _ in range(M):
    p, x = map(int, input().split())
    print(sumt - T[p-1] + x)
