N = int(input())
A = set(map(int, input().split()))
ans = 0
while True:
    if not ans in A:
        print(ans)
        break
    ans += 1