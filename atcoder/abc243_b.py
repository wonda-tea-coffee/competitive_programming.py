N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
seta = set(A)
setb = set(B)
cnt1 = 0
cnt2 = 0
for i in range(N):
    if not A[i] in setb: continue
    if A[i] == B[i]:
        cnt1 += 1
    else:
        cnt2 += 1
print(cnt1)
print(cnt2)
