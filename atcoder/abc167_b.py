A, B, C, K = map(int, input().split())
p1 = min(A, K)
K -= p1
K -= min(B, K)
pm1 = min(C, K)
print(p1 - pm1)