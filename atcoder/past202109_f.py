N = int(input())
S = "*" + input()

if S.count("0") == 1:
    print(-1)
    exit()

A = [-1] * (N+1)
z = []

for i in range(1, N+1):
    if S[i] == "0":
        z.append(i)
    else:
        A[i] = i

lz = len(z)
for i in range(lz):
    A[z[i]] = z[(i+1)%lz]

print(*A[1:])
