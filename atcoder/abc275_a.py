N = int(input())
H = list(map(int, input().split()))

mi = -1
m = 0
for i in range(N):
    if H[i] > m:
        mi = i+1
        m = H[i]
print(mi)
