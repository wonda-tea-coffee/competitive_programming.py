A = sorted(list(map(int, input().split())))
K = int(input())
A[-1] *= 2**K
print(sum(A))