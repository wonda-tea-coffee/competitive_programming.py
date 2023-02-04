N = int(input())

ans = []
for i in range(1, N+1):
    if i % 3 == 0 or str(i).count("3") > 0:
        ans.append(i)

print(*ans)