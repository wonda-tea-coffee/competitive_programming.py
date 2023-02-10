N, K = map(int, input().split())
print(len(list(filter(lambda x: int(x) >= K, input().split()))))