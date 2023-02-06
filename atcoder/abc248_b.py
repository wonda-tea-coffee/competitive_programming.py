import math
A, B, K = map(int, input().split())
print(math.ceil((math.log(B, 10) - math.log(A, 10)) / math.log(K, 10)))