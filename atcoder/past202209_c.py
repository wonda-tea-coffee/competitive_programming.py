P = [[0]+list(map(int, input().split())) for _ in range(3)]
ans = [0]*19
for i in range(1, 7):
	for j in range(1, 7):
		for k in range(1, 7):
			ans[i+j+k] += P[0][i]/100 * P[1][j]/100 * P[2][k]/100

for i in range(1, 19):
    print("%0.6f" % ans[i])
