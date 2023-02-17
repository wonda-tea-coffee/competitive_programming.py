INF = float("inf")

def round255(n):
	if n > 255:
		return 255
	elif n < 0:
		return 0
	else:
		return n

while True:
	N, M = map(int, input().split())
	if N == M == 0: break
	# print(N, M)
	C = tuple(int(input()) for _ in range(M))
	X = tuple(int(input()) for _ in range(N))

	dp = [INF]*256
	dp[128] = 0
	for x in X:
		dp2 = list(dp)
		dp = [INF]*256
		for j in range(256):
			for c in C:
				to = round255(j+c)
				dp[to] = min(dp[to], dp2[j] + (x-to)**2)
	print(min(dp))
