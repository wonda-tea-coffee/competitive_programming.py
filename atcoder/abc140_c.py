N = int(input())
B = list(map(int, input().split()))
A = [B[0]]
mae = -1
for i in range(1, N-1):
    A.append(min(B[i-1], B[i]))

A.append(B[-1])
# print(A) # 1,2,...,N-2
print(sum(A))
