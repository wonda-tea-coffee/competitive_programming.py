# 1, 2, 3, 4, (5), 6, (7), 8, (9), 10, (11), 12
N = int(input())
a = sorted(list(map(int, input().split())))
print(sum(a[N::2]))