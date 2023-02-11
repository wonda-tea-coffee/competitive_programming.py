N = int(input())

# X = 1

# K = 1:  (3^1 + 1) * 3^29
# K = 2:  (3^2 + 1) * 3^28
# ...
# K = 30: (3^30 + 1) * 3^0

for k in range(1, 31):
    # print(k, (3**k + 1) * 3**(30-k))
    if (3**k + 1) * 3**(30-k) == N:
        print(k)
        exit()

print(-1)
