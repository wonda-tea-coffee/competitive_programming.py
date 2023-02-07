k = 0
N = int(input())
while 2**k <= N:
    k += 1
print(k-1)