import math

# 1(1)
# 2, 1, 2(3)
# 3, 2, 1, 2, 3(5)
# 4, 3, 2, 1, 2, 3, 4(7)

# √N <= M
# 10: 4
# N = 10 then M = 4
# a = N - (M-1)^2 = 10 - 3^2 = 1
# b = 2*M - 1 = 2*4 - 1 = 7
# if a <= b//2:
#   M-a+1
# else:
#   a-M+1

N = int(input())
M = math.ceil(math.sqrt(N))
a = N - (M-1)**2
b = 2*M - 1
if a <= b//2:
    print(M-a+1)
else:
    print(a-M+1)
