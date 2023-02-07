N, A, B = map(int, input().split())
m = min(N, 5)
print(m*B + (N-m)*A)