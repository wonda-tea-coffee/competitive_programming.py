import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = []
for i in range(N):
    S.append(
        (-(A[i]+B[i]), -A[i], i+1)
    )

S.sort()
print(*list(map(lambda x: x[2], S)))
