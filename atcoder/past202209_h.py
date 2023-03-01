import sys
input = lambda: sys.stdin.readline().rstrip()

# 銀貨の枚数は十分
N, X = map(int, input().split())
A = []
B = []
C = []
for _ in range(N):
	a, b, c = map(int, input().split())
	A.append(a)
	B.append(b)
	C.append(c)

dp_gold = [0]*(X+1)
dp_silver = [0]*(X+1)
dp_silver[X] = 10**9

for i in range(N):
	ndp_gold = list(dp_gold)
	ndp_silver = list(dp_silver)
	for j in range(X+1):
		if j + B[i] > X: continue
		if dp_silver[j + B[i]] < A[i]: continue

		if dp_gold[j] < dp_gold[j + B[i]] + C[i]:
			ndp_gold[j] = dp_gold[j + B[i]] + C[i]
			ndp_silver[j] = dp_silver[j + B[i]] - A[i]
		elif dp_gold[j] == dp_gold[j + B[i]] + C[i]:
			if dp_silver[j] < dp_silver[j + B[i]] - A[i]:
				ndp_gold[j] = dp_gold[j + B[i]] + C[i]
				ndp_silver[j] = dp_silver[j + B[i]] - A[i]

	dp_gold = ndp_gold
	dp_silver = ndp_silver

ans_gold = 0
ans_silver = 0
ans_copper = -1
for i in range(X+1):
    # 金、銀ともに同数の場合は昇順に見ているためans_copperには大きな値が選ばれる、はず
    if dp_gold[i] > ans_gold or (dp_gold[i] == ans_gold and ans_silver <= dp_silver[i]):
        ans_gold = dp_gold[i]
        ans_silver = dp_silver[i]
        ans_copper = i

if ans_copper == -1:
    print(0, 10**9, X)
else:
    print(ans_gold, ans_silver, ans_copper)
