# a = 10^3
# b = 1000a = 10^6
# c = 1000b = 10^9
# d = 10^12
# ...
# z = 10^78
# 999z = 999 * 10^78 < 1000 * 10^78 = 10^81

import string

a = int(input())

cnt = 0
while len(str(a)) > 3:
    cnt += 1
    a //= 1000

print(str(a) + string.ascii_lowercase[cnt-1])
