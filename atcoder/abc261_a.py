L1, R1, L2, R2 = map(int, input().split())
print(max(0, len(set(range(L1, R1+1)) & set(range(L2, R2+1)))-1))