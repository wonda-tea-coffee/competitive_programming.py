S, T = map(int, input().split())
ans = 0
for a in range(S+1):
    for b in range(S+1):
        if a + b > S: break
        for c in range(S+1):
            if a + b + c > S: break

            if a * b * c <= T:
                # print(a, b, c)
                ans += 1

print(ans)