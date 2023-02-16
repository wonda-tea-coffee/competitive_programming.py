import math
N, M, K, Q = map(int, input().split())

A = []
B = []
for _ in range(N):
    p, t = map(int, input().split())
    if t == 0:
        A.append(p)
    else:
        B.append(p)

A.sort()
B.sort()
AS = [0]
BS = [0]
suma = 0
sumb = 0
for a in A:
    suma += a
    AS.append(suma)
for b in B:
    sumb += b
    BS.append(sumb)

# print(A, AS)
# print(B, BS)
ans = 10**100
for i in range(min(len(A), M)+1):
    if M - i > len(B): continue

    # BからM-i個取る
    sumb = BS[M-i] + math.ceil((M-i)/K)*Q

    ans = min(ans, AS[i] + sumb)

print(ans)
