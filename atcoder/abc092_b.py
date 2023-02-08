N = int(input())
D, X = map(int, input().split())
ans = X

for i in range(1, N+1):
    Ai = int(input())
    # k*Ai+1 <= D
    # k*Ai <= D-1
    # k <= (D-1)/Ai
    v = (D-1)//Ai + 1
    # print(i, v)
    ans += v

print(ans)