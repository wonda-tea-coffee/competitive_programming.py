N = int(input())
A = [-1] + list(map(int, input().split()))
ans = set(range(1, N+1))

for i in range(1, N+1):
    if i in ans and A[i] in ans:
        ans.remove(A[i])

print(len(ans))
print(*sorted(ans), sep=" ")
