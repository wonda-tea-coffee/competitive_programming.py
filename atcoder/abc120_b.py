A, B, K = map(int, input().split())

d = []
for i in range(1, min(A, B)+1):
    if A % i == 0 and B % i == 0:
        d.append(i)

print(d[len(d)-K])
