N = int(input())
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    # a, a+1, a+2, ..., b(=a+k)
    # a*(k+1) + k*(k+1)/2
    # b=a+k <=> k=b-a
    k = b - a
    ans += a*(k+1) + k*(k+1)//2

print(ans)