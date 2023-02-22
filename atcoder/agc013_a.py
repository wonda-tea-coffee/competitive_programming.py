N = int(input())
A = list(map(int, input().split()))
ans = 1
f = 0
for i in range(1, N):
    if f == 0:
        if A[i-1] == A[i]:
            pass
        elif A[i-1] < A[i]:
            f = 1
        else:
            f = -1
    elif f == 1:
        if A[i-1] <= A[i]:
            pass
        else:
            f = 0
            ans += 1
    else:
        if A[i-1] >= A[i]:
            pass
        else:
            f = 0
            ans += 1

print(ans)
