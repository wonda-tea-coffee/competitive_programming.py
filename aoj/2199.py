INF = float("inf")

while True:
	N, M = map(int, input().split())
	if N == M == 0: break
	# print(N, M)
	C = tuple(int(input()) for _ in range(M))
	X = tuple(int(input()) for _ in range(N))

	p = set()
	for j in range(256):
		for c in C:
			if j+c < 0:
				to = 0
			elif j+c > 255:
				to = 255
			else:
				to = j+c
			p.add((to, j))
	dp = [INF]*256
	dp[128] = 0
	for x in X:
		dp2 = list(dp)
		dp = [INF]*256
		for to, j in p:
			dp[to] = min(dp[to], dp2[j] + (x-to)**2)
	print(min(dp))
