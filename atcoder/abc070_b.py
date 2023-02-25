A, B, C, D = map(int, input().split())

print(max(len(set(range(A, B+1)) & set(range(C, D+1))) - 1, 0))