X = int(input())
c = 100
ans = 0

while c < X:
    c += c // 100
    ans += 1

print(ans)
