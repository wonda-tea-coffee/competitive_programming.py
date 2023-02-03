A, B, C = map(int, input().split())
C -= min(C, A-B)
print(C)