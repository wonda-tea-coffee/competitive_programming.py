n = list(map(int, input().split()))

ansmax = -10**100
ansmin = 10**100
for i in range(len(n)):
    for j in range(i+1, len(n)):
        ansmax = max(ansmax, n[i] * n[j])
        ansmin = min(ansmin, n[i] * n[j])

print(ansmin, ansmax)
