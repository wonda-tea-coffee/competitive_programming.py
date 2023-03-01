import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
C = []
for _ in range(N):
    input() # Ci
    C.append(set(map(int, input().split())))
Q = int(input())
res = []
for _ in range(Q):
	D = int(input())
	Y = set(map(int, input().split()))

	ans = -1
	maxa = 0
	for i in range(N):
		if A[i] <= maxa: continue
		if C[i] & Y: continue
		maxa = A[i]
		ans = i+1

	res.append(ans)

for r in res:
    print(r)