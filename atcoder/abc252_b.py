import sys
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(lambda x: int(x)-1, input().split()))
uma = 0
umami = set()
for i in range(N):
    if uma < A[i]:
        uma = A[i]
        umami = set({i})
    elif uma == A[i]:
        umami.add(i)

if umami & B:
    print("Yes")
else:
    print("No")